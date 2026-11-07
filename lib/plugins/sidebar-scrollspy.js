(function (global) {
  "use strict";

  // docsify 插件：左侧目录跟随正文滚动定位（scrollspy）。
  //
  // 背景：docsify 4.13.1 内置的 scrollActiveSidebar 用「当前 hash 路径」去匹配
  // 「侧边栏链接」，而侧边栏链接经 toURL 生成时统一去掉了 .md 后缀；一旦 URL
  // 带 .md（目录大纲、正文互链、分享链接等入口都会产生），内置匹配永远落空，
  // 左侧目录便不再跟随正文定位。
  // 本插件接管同步：路径统一规范化后再匹配，滚动时高亮当前小节并滚动侧边栏，
  // 切换页面后也会把当前章节滚进侧边栏可视区。

  var TOP_OFFSET = 60; // 标题进入距视口顶部该距离内，视为“已读到该节”
  var VIEWPORT_EDGE = 24; // 激活项与侧边栏可视区边缘的余量（px）

  var spy = null;
  var ticking = false;
  var listenerInstalled = false;

  // 将 hash 路径规范化为可比较的形式：去 #、去查询串、去 .md 后缀并解码
  function normalizePath(rawPath) {
    var path = String(rawPath || "");
    if (path.charAt(0) === "#") {
      path = path.slice(1);
    }
    var queryAt = path.indexOf("?");
    if (queryAt >= 0) {
      path = path.slice(0, queryAt);
    }
    path = path.replace(/\.md$/i, "");
    try {
      path = decodeURIComponent(path);
    } catch (error) {
      // 解码失败时保留原样继续比较
    }
    return path;
  }

  function decodeId(value) {
    try {
      return decodeURIComponent(value);
    } catch (error) {
      return value;
    }
  }

  // docsify 首页路由是 "/"，而侧边栏链接使用等价的 "/README"
  function isSamePage(a, b) {
    if (a === b) {
      return true;
    }
    return (a === "/" || a === "/README") && (b === "/" || b === "/README");
  }

  function prefersSmoothScroll() {
    return !(
      global.matchMedia &&
      global.matchMedia("(prefers-reduced-motion: reduce)").matches
    );
  }

  // 取链接所属的 <li>；_sidebar.md 中有空行的分组会被渲染成 li > p > a，
  // 此时回到外层 li 上，与 docsify 的 li.active 高亮样式保持一致
  function linkItem(link) {
    return (link.closest && link.closest("li")) || link.parentNode;
  }

  // 疏松列表结构（li > p > a）下，高亮样式需补充一条选择器才能生效
  function ensureStyle() {
    if (document.getElementById("sidebar-scrollspy-style")) {
      return;
    }
    var style = document.createElement("style");
    style.id = "sidebar-scrollspy-style";
    style.textContent =
      ".sidebar ul li.active > p > a { color: var(--accent, #42b983); }";
    document.head.appendChild(style);
  }

  function ScrollSpy() {
    this.ready = false;
    this.pageLi = null;
    this.sectionLinks = {}; // 标题 id -> 侧边栏小节 li
    this.headings = [];
    this.activeLi = null;
  }

  // 每次页面渲染完成后重建索引（sidebar-nav 与正文都会被整体重渲染）
  ScrollSpy.prototype.collect = function () {
    var sidebar = document.querySelector(".sidebar");
    var content = document.querySelector(".markdown-section");
    this.ready = !!(sidebar && content);
    if (!this.ready) {
      return;
    }

    var pagePath = normalizePath(global.location.hash);
    this.sectionLinks = {};
    this.pageLi = null;
    this.activeLi = null;

    var links = sidebar.querySelectorAll(".sidebar-nav a[href^='#']");
    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      var href = link.getAttribute("href") || "";
      var queryAt = href.indexOf("?");
      var linkPath = normalizePath(
        queryAt >= 0 ? href.slice(0, queryAt) : href
      );
      if (!isSamePage(linkPath, pagePath)) {
        continue;
      }
      if (queryAt < 0) {
        this.pageLi = linkItem(link); // 当前页自身的链接（无 ?id=）
        continue;
      }
      var idMatch = /[?&]id=([^&]*)/.exec(href);
      if (idMatch) {
        this.sectionLinks[decodeId(idMatch[1])] = linkItem(link);
      }
    }

    this.headings = [];
    var headings = content.querySelectorAll("h1[id], h2[id], h3[id], h4[id]");
    for (var j = 0; j < headings.length; j++) {
      this.headings.push(headings[j]);
    }
  };

  // 返回当前读到的位置：最后一个已滚过阈值、且在目录中有对应小节的标题
  ScrollSpy.prototype.currentSectionLi = function () {
    var li = null;
    for (var i = 0; i < this.headings.length; i++) {
      var heading = this.headings[i];
      if (heading.getBoundingClientRect().top > TOP_OFFSET) {
        break;
      }
      var candidate = this.sectionLinks[heading.id];
      if (candidate) {
        li = candidate;
      }
    }
    return li;
  };

  ScrollSpy.prototype.setActive = function (li) {
    if (this.activeLi === li) {
      return false;
    }
    var sidebar = document.querySelector(".sidebar");
    var actives = sidebar ? sidebar.querySelectorAll("li.active") : [];
    for (var i = 0; i < actives.length; i++) {
      actives[i].classList.remove("active");
    }
    if (li) {
      li.classList.add("active");
    }
    this.activeLi = li;
    return true;
  };

  // 让侧边栏自身滚动，保证激活项可见（手动计算，避免 scrollIntoView 波及正文）
  ScrollSpy.prototype.scrollSidebar = function (li) {
    var sidebar = document.querySelector(".sidebar");
    if (!sidebar || !li) {
      return;
    }
    var sidebarTop = sidebar.getBoundingClientRect().top;
    var rect = li.getBoundingClientRect();
    var liTop = rect.top - sidebarTop + sidebar.scrollTop;
    var viewTop = sidebar.scrollTop + VIEWPORT_EDGE;
    var viewBottom = sidebar.scrollTop + sidebar.clientHeight - VIEWPORT_EDGE;
    if (liTop >= viewTop && liTop + rect.height <= viewBottom) {
      return; // 已在可视区内
    }
    var target = liTop - (sidebar.clientHeight - rect.height) / 2;
    target = Math.max(
      0,
      Math.min(target, sidebar.scrollHeight - sidebar.clientHeight)
    );
    target = Math.round(target);
    if (
      typeof sidebar.scrollTo === "function" &&
      "scrollBehavior" in document.documentElement.style
    ) {
      sidebar.scrollTo({
        top: target,
        behavior: prefersSmoothScroll() ? "smooth" : "auto",
      });
    } else {
      sidebar.scrollTop = target;
    }
  };

  ScrollSpy.prototype.update = function (alignSidebar) {
    if (!this.ready) {
      return;
    }
    // 侧边栏收起（移动端或手动关闭）时无需同步
    if (document.body.classList.contains("close")) {
      return;
    }
    var li = this.currentSectionLi() || this.pageLi;
    if (!li) {
      return;
    }
    if (this.setActive(li) || alignSidebar) {
      this.scrollSidebar(li);
    }
  };

  function onScroll() {
    if (ticking || !spy || !spy.ready) {
      return;
    }
    ticking = true;
    global.requestAnimationFrame(function () {
      ticking = false;
      spy.update(false);
    });
  }

  var install = function (hook, vm) {
    ensureStyle();

    hook.doneEach(function () {
      var config = (vm && vm.config && vm.config.sidebarScrollspy) || {};
      if (config.enabled === false) {
        return;
      }
      if (!spy) {
        spy = new ScrollSpy();
      }
      spy.collect();
      spy.update(true);
    });

    if (!listenerInstalled) {
      listenerInstalled = true;
      global.addEventListener("scroll", onScroll, { passive: true });
    }
  };

  global.$docsify = global.$docsify || {};
  global.$docsify.plugins = (global.$docsify.plugins || []).concat(install);
})(window);
