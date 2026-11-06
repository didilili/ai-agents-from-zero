(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (root && root.document) api.install(root);
})(typeof window === "undefined" ? null : window, function () {
  "use strict";

  var PREFIX = "/translations/en/";

  function pageInfo(path) {
    path = String(path || "/")
      .replace(/^#/, "")
      .split("?")[0];
    try {
      path = decodeURIComponent(path);
    } catch (error) {
      // A malformed URL should not stop the rest of the documentation site.
    }
    if (path.charAt(0) !== "/") path = "/" + path;
    var language = path.indexOf(PREFIX) === 0 ? "en" : "zh";
    var source = language === "en" ? path.slice(PREFIX.length) : path.slice(1);
    source = source || "README.md";
    if (!/\.md$/.test(source)) source += ".md";
    return { language: language, source: source };
  }

  function switchTarget(path, language, metadata) {
    var source = pageInfo(path).source;
    if (
      language === "en" &&
      (!metadata ||
        !metadata[source] ||
        metadata[source].language_code !== "en")
    ) {
      return null;
    }
    var prefix = language === "en" ? PREFIX : "/";
    return (
      "#" +
      prefix +
      (source === "README.md"
        ? ""
        : source.split("/").map(encodeURIComponent).join("/"))
    );
  }

  function resolveImageSource(src, path, basePath, pageURL) {
    if (
      pageInfo(path).language !== "en" ||
      !src ||
      /^(?:[a-z][\w+.-]*:|\/\/|\/|#)/i.test(src.trim())
    ) {
      return src;
    }
    var base = new URL(basePath || "./", pageURL);
    var documentPath =
      "translations/en/" +
      pageInfo(path).source.split("/").map(encodeURIComponent).join("/");
    return new URL(src, new URL(documentPath, base)).href;
  }

  function expiredImageNotice(src, language, now) {
    var url;
    try {
      url = new URL(src);
    } catch (error) {
      return null;
    }
    var expires = Number(url.searchParams.get("x-expires"));
    if (
      url.hostname !== "p9-official-plugin-sign.byteimg.com" ||
      !Number.isFinite(expires) ||
      expires <= 0 ||
      expires * 1000 > (now === undefined ? Date.now() : now)
    ) {
      return null;
    }
    return language === "en"
      ? "This example image's temporary link has expired. Run the text-to-image node again to get a fresh link. The local screenshot above shows the recorded node output."
      : "此示例图片的临时链接已过期，请重新运行文生图节点获取新链接。上方的本地截图保留了当时的节点输出。";
  }

  function repairRenderedImages(html, path, basePath, pageURL, document) {
    if (!/<img\s/i.test(html)) return html;
    var template = document.createElement("template");
    template.innerHTML = html;
    var changed = false;
    template.content.querySelectorAll("img[src]").forEach(function (img) {
      if (img.closest("pre, code")) return;
      var src = img.getAttribute("src");
      var notice = expiredImageNotice(src, pageInfo(path).language);
      if (notice) {
        var message = document.createElement("span");
        message.setAttribute("role", "note");
        message.textContent = notice;
        img.replaceWith(message);
        changed = true;
        return;
      }
      var target = resolveImageSource(src, path, basePath, pageURL);
      if (target !== src) {
        img.setAttribute("src", target);
        changed = true;
      }
    });
    return changed ? template.innerHTML : html;
  }

  function install(root) {
    var document = root.document;
    var config = root.$docsify;
    var initialLanguage = pageInfo(root.location.hash).language;
    var english = initialLanguage === "en";
    var subMaxLevel = config.subMaxLevel;
    var metadata = {};
    var metadataFailed = {};
    var panel;
    var toggle;
    var menu;
    var links = {};
    var status;
    var requests = {};

    config.alias = Object.assign({}, config.alias, {
      "/translations/en/(.*)_sidebar.md": "/_sidebar.en.md",
    });
    config.search.placeholder = {
      "/translations/en/": "Search documentation",
      "/": "搜索文档",
    };
    config.search.noData = {
      "/translations/en/": "No results found",
      "/": "未找到结果",
    };
    config.search.pathNamespaces = ["/translations/en"];
    config.nameLink = english ? "#/translations/en/" : "#/";
    document.documentElement.lang = english ? "en" : "zh-CN";
    if (english) {
      config.name = "AI Agents From Zero";
      config.pagination.previousText = "Previous";
      config.pagination.nextText = "Next";
      config.copyCode = {
        buttonText: "Copy",
        errorText: "Error",
        successText: "Copied",
      };
      config.count.language = "english";
      config.giscus.lang = "en";
      config.announcementBubble.text =
        "MianStack is live! Interview reports, technical Q&A, and project breakdowns. Free and open source — start practicing!";
    }

    // Some Docsify plugins capture their language options once on initialization.
    // Reload only when crossing languages so all interface text stays consistent.
    root.addEventListener("hashchange", function () {
      if (pageInfo(root.location.hash).language !== initialLanguage)
        root.location.reload();
    });

    function loadTranslation(source) {
      if (!requests[source]) {
        var url = new URL(
          (config.basePath || "./") +
            "translations/en/" +
            source.split("/").map(encodeURIComponent).join("/"),
          root.location.href,
        );
        requests[source] = root
          .fetch(url, { method: "HEAD" })
          .then(function (response) {
            if (
              response.ok &&
              !/text\/html/i.test(response.headers.get("Content-Type") || "")
            ) {
              metadata[source] = { language_code: "en" };
            } else if (response.status !== 404) {
              metadataFailed[source] = true;
            }
          })
          .catch(function () {
            metadataFailed[source] = true;
          });
      }
      return requests[source];
    }

    function updateLinks() {
      if (!panel) return;
      var path = root.location.hash;
      var current = pageInfo(path).language;
      toggle.title =
        current === "en" ? "Change language (English)" : "切换语言（简体中文）";
      toggle.setAttribute(
        "aria-label",
        english
          ? "Change language, current language English"
          : "切换语言，当前为简体中文",
      );
      ["zh", "en"].forEach(function (language) {
        var link = links[language];
        link.href =
          switchTarget(path, language, metadata) ||
          switchTarget(path, "zh", metadata);
        if (language === current) link.setAttribute("aria-current", "page");
        else link.removeAttribute("aria-current");
      });
    }

    function setOpen(open, returnFocus) {
      if (!menu) return;
      menu.hidden = !open;
      toggle.setAttribute("aria-expanded", String(open));
      if (returnFocus) toggle.focus();
    }

    function mount() {
      if (panel) return;
      panel = document.createElement("nav");
      panel.className = "language-switch";
      panel.setAttribute("aria-label", "语言 / Language");
      toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "language-switch__toggle";
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-controls", "language-switch-menu");
      toggle.innerHTML =
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 5h12M7 2h1m-3 6 6 6m-7 0 6-6 2-3m10 17-5-10-5 10m2-4h6"/></svg>';
      toggle.addEventListener("click", function () {
        setOpen(menu.hidden);
      });
      toggle.addEventListener("keydown", function (event) {
        if (event.key === "ArrowDown" || event.key === "ArrowUp") {
          event.preventDefault();
          setOpen(true);
          var items = menu.querySelectorAll("a");
          items[event.key === "ArrowDown" ? 0 : items.length - 1].focus();
        }
      });
      panel.appendChild(toggle);
      menu = document.createElement("div");
      menu.className = "language-switch__menu";
      menu.id = "language-switch-menu";
      menu.hidden = true;
      ["zh", "en"].forEach(function (language) {
        var link = document.createElement("a");
        link.textContent = language === "zh" ? "简体中文" : "English";
        link.hreflang = language === "zh" ? "zh-CN" : "en";
        link.lang = link.hreflang;
        var check = document.createElement("span");
        check.className = "language-switch__check";
        check.setAttribute("aria-hidden", "true");
        check.textContent = "✓";
        link.appendChild(check);
        link.addEventListener("click", function (event) {
          if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey)
            return;
          event.preventDefault();
          var clickedPath = root.location.hash;
          if (pageInfo(clickedPath).language === language) {
            setOpen(false, true);
            return;
          }
          loadTranslation(pageInfo(clickedPath).source).then(function () {
            if (root.location.hash !== clickedPath || menu.hidden) return;
            var target = switchTarget(clickedPath, language, metadata);
            if (target) {
              status.hidden = true;
              setOpen(false, true);
              root.location.hash = target;
            } else {
              status.textContent = metadataFailed[pageInfo(clickedPath).source]
                ? "暂时无法确认英文译文，请刷新后重试。"
                : "本章英文版尚未提供，继续显示中文。";
              status.hidden = false;
            }
          });
        });
        links[language] = link;
        menu.appendChild(link);
      });
      status = document.createElement("p");
      status.className = "language-switch__status";
      status.setAttribute("role", "status");
      status.hidden = true;
      menu.appendChild(status);
      panel.appendChild(menu);
      document.body.appendChild(panel);
      menu.addEventListener("keydown", function (event) {
        if (event.key !== "ArrowDown" && event.key !== "ArrowUp") return;
        event.preventDefault();
        var items = Array.from(menu.querySelectorAll("a"));
        var index = items.indexOf(document.activeElement);
        var next = index + (event.key === "ArrowDown" ? 1 : -1);
        items[(next + items.length) % items.length].focus();
      });
      document.addEventListener("pointerdown", function (event) {
        if (!panel.contains(event.target)) setOpen(false);
      });
      document.addEventListener("focusin", function (event) {
        if (!panel.contains(event.target)) setOpen(false);
      });
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && !menu.hidden) {
          event.preventDefault();
          setOpen(false, true);
        }
      });
      updateLinks();
      loadTranslation(pageInfo(root.location.hash).source).then(updateLinks);
    }

    config.plugins = (config.plugins || []).concat(function (hook, vm) {
      hook.mounted(mount);
      hook.beforeEach(function (markdown) {
        if (english) {
          vm.config.subMaxLevel =
            pageInfo(vm.route.path).source === "README.md" ? 0 : subMaxLevel;
        }
        return markdown;
      });
      hook.afterEach(function (html) {
        // Markdown images already have Docsify's content base. Resolve the
        // remaining relative HTML sources before inserting the article.
        return repairRenderedImages(
          html,
          vm.route.path,
          config.basePath,
          root.location.href,
          document,
        );
      });
      hook.doneEach(function () {
        mount();
        updateLinks();
        setOpen(false);
        loadTranslation(pageInfo(root.location.hash).source).then(updateLinks);
        if (status) status.hidden = true;
        var search = document.querySelector('.search input[type="search"]');
        if (search)
          search.setAttribute(
            "aria-label",
            english ? "Search documentation" : "搜索文档",
          );
        var menu = document.querySelector(".sidebar-toggle");
        if (menu)
          menu.setAttribute(
            "aria-label",
            english ? "Toggle navigation" : "切换目录",
          );
      });
    });
  }

  return {
    pageInfo: pageInfo,
    switchTarget: switchTarget,
    resolveImageSource: resolveImageSource,
    expiredImageNotice: expiredImageNotice,
    repairRenderedImages: repairRenderedImages,
    install: install,
  };
});
