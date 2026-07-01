import MarkdownIt from "markdown-it";
import hljs from "highlight.js";

import "highlight.js/styles/atom-one-dark.css";
import ClipboardJS from "clipboard"; //复制插件

//Markdown解析
const md = new MarkdownIt({
  html: false,
  linkify: true,
  typographer: true,
  breaks: true,
  highlight: function (str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        let highlightedHtml = hljs.highlight(str, { language: lang }).value;
        // 生成行号
        let lineNum = highlightedHtml.split("\n").length - 1;
        let lineNumbersRowsStart = `<span aria-hidden="true" class="line-numbers-rows">`;
        let lineNumbersRowsEnd = `</span>`;
        for (let i = 0; i < lineNum; i++) {
          lineNumbersRowsStart += `<span></span>`;
        }
        const lineNumbersRows = lineNumbersRowsStart + lineNumbersRowsEnd;

        let languageName = `<b class="language-name">${lang}</b>`;

        // 当前时间加随机数生成唯一的id标识
        var d = new Date().getTime();
        if (
          window.performance &&
          typeof window.performance.now === "function"
        ) {
          d += performance.now();
        }
        const codeIndex = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
          /[xy]/g,
          function (c) {
            var r = (d + Math.random() * 16) % 16 | 0;
            d = Math.floor(d / 16);
            return (c == "x" ? r : (r & 0x3) | 0x8).toString(16);
          }
        );
        // 复制功能需要一个textarea（这个id需要前面加个字母啥的，不能以数字开头）
        let textAreaHtml = `<textarea class="copy-textarea" id="copy${codeIndex}">${str}</textarea>`;

        let copyButton = `<button class="copy-btn iconfont icon-fuzhi"  data-clipboard-action="copy" data-clipboard-target="#copy${codeIndex}" type="button">copy</button>`;

        /* 如果返回的不含pre code标签，它会自己加上；如果返回的含有pre code标签，它就不加了 */
        return `<div class="codeBlockHeader">${languageName}${copyButton}${textAreaHtml}</div><pre><code class="language-${lang} hljs">${highlightedHtml}</code>${lineNumbersRows}</pre>`;
      } catch (__) { }
    }
    return "";
  },
})
  .use(require("markdown-it-implicit-figures"))
  .use(require("markdown-it-sub"))
  .use(require("markdown-it-sup"))
  .use(require("markdown-it-mark"))
  .use(require("markdown-it-abbr"))
  .use(require("markdown-it-container"))
  .use(require("markdown-it-deflist"))
  .use(require("markdown-it-emoji"))
  .use(require("markdown-it-footnote"))
  .use(require("markdown-it-ins"))
  .use(require("markdown-it-katex-external"))
  .use(require("markdown-it-task-lists"));

const copyButton = document.querySelectorAll(".copy-btn");
const clipboard = new ClipboardJS(".copy-btn");
function handleClick(event) {
  // 取消所有按钮的选中状态
  copyButton.forEach((button) => button.classList.remove("selected"));
  // 选中点击的按钮
  event.target.classList.add("selected");
  // 在这里添加你希望执行的操作
}
copyButton.forEach((button) => {
  button.addEventListener("click", handleClick);
});
clipboard.on("success", function (e) {
  // ElMessage.success("复制成功");
  e.clearSelection();
});
clipboard.on("error", function (e) {
  // ElMessage.error("复制失败");
});

export default md;
