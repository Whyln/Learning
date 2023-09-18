[TOC]

# 自制Markdown教程[^1]

## Markdown介绍

### Markdown是一种轻量级的<u>标记语言</u>

可用于在纯文本文档中添加格式化元素，使之产生美观大方的排版。其相较于 Word 是一款**所见非所得**的文本编辑器。

1. Markdown 是**纯文本可移植**的。几乎可以使用任何应用程序打开包含 Markdown 格式的文本文件。如果你不喜欢当前使用的 Markdown 应用程序了，则可以将 Markdown 文件导入另一个 Markdown 应用程序中。这与 Microsoft Word 等文字处理应用程序形成了鲜明的对比，Microsoft Word 将你的内容锁定在专有文件格式中。
2. Markdown 是**独立于平台**的。你可以在运行任何操作系统的任何设备上创建 Markdown 格式的文本。

### Markdown的工作原理

在使用 Markdown 格式书写时，文本内容存储在拓展名为 `.md` 或 `.markdown` 的纯文本文件中。然后通过 *Markdown 解析器* 将获取到的 Markdown 格式的文本输出为 HTML 格式。此时，就可以在 Web 浏览器中查看你的文档，或者将其与样式表组合并打印。你可以在下图看到此过程的直观表示。

![The Markdown Process](./img/5.png)

至于*Markdown解释器*的实现这里有一个github上的用python写的项目[python-Markdown](https://github.com/Python-Markdown/markdown)（我pull下来了，正在学习，~~以后有机会自己搞一个~~

### Markdown编辑器

在线编辑器如*[在线markdown编辑器](https://markdown.com.cn/editor/)*，本地的有**[Notepad+](https://notepad-plus-plus.org)*、*Vscode*(万能)、*Typora*(Markdown专用编辑器，好用但收费)等

下面介绍如何用Vscode写Markdown:需要下载以下插件
1. *Markdown All in One*  ——使Vscode支持基本所有Markdown语法（支持 `Mermaid` ）,并提供自动代码补全,快捷键功能
    <img src="./img/1.png" alt="1"  />
2. *Markdown Preview Ehanced*   ——用于渲染当前编写文档的效果同步预览 
    <img src="./img/2.png" alt="2"  />
3. *Markdown PDF* ——将`.md`文件导出为PDF
    <img src="./img/4.png" alt="4"  />
4. *Paste Image*   ——用于快速引用图片至Markdown文档
    <img src="./img/3.png" alt="3"  />

-----------------------------------------

## Markdown基础语法
> 声明:目前Markdown语法还没有统一的规范，以下语法为我个人学习所得，仅供参考
###  标题(`#`)

要创建标题，请在单词或短语前面添加井号 (`#`) 。`#` 的数量代表标题的级别。共六级

```Markdown
# Heading level 1
## Heading level 2
### Heading level 3
```
> **注意**：请用一个空格在 `#` 和标题之间进行分隔。

### 段落与换行( `<br>`)

要创建段落，请使用空白行将一行或多行文本进行分隔。

要换行，在一行的末尾添加两个或多个空格，然后按回车键(也可用`<br>`)。

### 强调(`*`)

要*斜体* 、**加粗**、***加粗并斜体***，需要用`*`包裹内容

```markdown
*TEXT1* —— 斜体
**TEXT2** —— 加粗
***TEXT3*** —— 加粗并斜体
```

### 删除线(`~`)和下划线(`<u></u>`)

您可以用双波浪号`~~`包裹内容来给内容添加~~删除线~~。
您可以用html中的<u>来添加下划线</u>

```markdown
~~TEXT~~
<u>TEXT</u>
```

### 列表(`x. `、`-`/`+`/`*`)

列表分为**有序列表**和**无序列表**：要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点`.`。

要创建无序列表，请在每个列表项前面添加破折号 `-`，或加号 `+`或者星号`*` 。

缩进一个或多个列表项可创建嵌套列表。

```markdown
有序列表
1. line1
	1. line1-1
    2. line1-2
2. line2
3. line3
无序列表
- line1
	- line1-1
	- line2-2
- line2
有序无序嵌套
1. line1
	- line1-1
	- line1-2
2. line2
```

### 任务列表(`- [ ] text`)

任务列表使您可以创建带有复选框的项目列表。在支持任务列表的Markdown应用程序中，复选框将显示在内容旁边。

要创建任务列表，请在任务列表项之前添加破折号`-`和方括号`[ ]`，并在`[ ]`前面加上空格。要选择一个复选框，请在方括号`[x]`之间添加 x 。

```markdown
- [ ] one
- [x] two
```

> 注意在`-`、`[]`、text间添加空格



### 表格(`|----|---|`)

要添加表格，请使用三个或多个连字符（`---`）创建每列的标题，并使用管道（`|`）分隔每列。您可以选择在表的任一端添加管道。

您可以通过在标题行中的连字符的左侧，右侧或两侧添加冒号（`:`），将列中的文本对齐到左侧，右侧或中心。

```markdown
| Syntax | Description | Test Text |
| :----- | :---------: | --------: |//分别是左、居中、右对齐
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

> 注意：在表格格子内enter换行不起作用，请使用`<br>`来进行换行操作

### 引用(`>`)

要创建块引用，请在段落前添加一个 `>` 符号。块引用可以包含多个段落。为段落之间的空白行添加一个 `>` 符号。

块引用可以嵌套。在要嵌套的段落前添加一个 `>>` 符号。

块引用可以包含其他 Markdown 格式的元素。但有时并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。

```markdown
引用
> line
多个段落的引用
> para1
>
> para2
嵌套引用
> line1
>> line1-1
> line2
带有其它元素的引用
> - line1
> - line2
```

### 代码与代码块( \`)

要将单词或短语表示为代码，请将其包裹在反引号 (``) 中。

如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号(````)中。

如果你引入的是代码块可以将代码包裹在三反引号当中(``````)从而可以提供代码高亮功能。

```markdown
`code` ——代码
``code `1` `` ——代码中存在`
```python
print("code")
```				——代码块并提供语法高亮
```

### 分割线(`-------`)

要创建分隔线，请在单独一行上使用三个或多个星号 (`***`)、破折号 (`---`) 或下划线 (`___`) ，并且不能包含其他内容。
```markdown

***

---

_________________

```

> **注意**：为了兼容性，请在分隔线的前后均添加空白行

### 链接(`[name](url "title")`)

链接文本放在中括号内，链接地址放在后面的括号中，链接title(鼠标悬停是显示的内容)可选。

超链接Markdown语法代码：`[超链接显示名](超链接地址 "超链接title")`

对应的HTML代码：`<a href="超链接地址" title="超链接title">超链接显示名</a>`   

同时也可以给`name`增加Markdown样式

```
[Markdown语法](https://markdown.com.cn "最好的markdown教程") ——链接markdown语法表示
```

示例[Markdown语法](https://markdown.com.cn "最好的markdown教程")

> 不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用`%20`代替空格。

### 图片(`![alt](url/path "title")`)

要添加图像，请使用感叹号 (`!`), 然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

插入图片Markdown语法代码：`![图片alt](图片链接 "图片title")`。

对应的HTML代码：`<img src="图片链接" alt="图片alt" title="图片title">`

同时也支持图片和链接的嵌套

``` markdown
![yileina](./img/yileina.jpg "cute") —— 图片
<img src="./img/yileina.jpg" alt="yileina" title="cute" style="zoom: 50%;" /> --用html代码可以调控大小
[![yileina](./img/yileina.jpg "cute")](https://markdown.com.cn) ——图片链接 
```

[![yileina](./img/yileina.jpg "cute")](https://markdown.com.cn)



### 脚注(`[^name]`)

脚注使您可以添加注释和参考，而不会使文档正文混乱。当您创建脚注时，带有脚注的上标数字会出现在您添加脚注参考的位置。读者可以单击链接以跳至页面底部的脚注内容。

要创建脚注参考，请在方括号（`[^1]`）内添加插入符号和标识符。标识符可以是数字或单词，但不能包含空格或制表符。标识符仅将脚注参考与脚注本身相关联-在输出中，脚注按顺序编号。

在括号内使用另一个插入符号和数字添加脚注，并用冒号和文本（`[^1]: My footnote.`）。您不必在文档末尾添加脚注。您可以将它们放在除列表，块引号和表之类的其他元素之外的任何位置。

```markdown
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
```

## Markdown拓展语法

### 内联html标签(直接使用)

对于 Markdown 涵盖范围之外的标签，都可以直接在文件里面用 HTML 本身。如需使用 HTML，不需要额外标注这是 HTML 或是 Markdown，只需 HTML 标签添加到 Markdown 文本中即可。

> 在 HTML 块级标签内不能使用 Markdown 语法。例如 `<p>italic and **bold**</p>` 将不起作用。

### 内联latex语法(`$code$`)

如果你生成优美的数学公式或其他更好看的内容，可以尝试使用latex的语法，可以将由与包裹的内容进行渲染并产生最终效果。***在markdown中使用LaTeX，内容都是写在一对"$"中。***

> 只有部分markdown解释器内置了latex渲染器

### 流程图(mermaid)

在markdown里你可以使用mermaid拓展工具来绘制流程图。你可以前往

[Markdown画图及Mermaid入门 - LYinMX - 博客园 (cnblogs.com)](https://www.cnblogs.com/LYinMX/p/13347646.html)学习语法

也可以前往官网[Mermaid | Diagramming and charting tool](https://mermaid.js.org/intro/)使用其live editor来帮助你

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
```

> 注：markdown中使用mermaid代码需要将包裹在代码块中并标注为mermaid

### 使用Emoji表情

有两种方法可以将表情符号添加到Markdown文件中：将表情符号复制并粘贴到Markdown格式的文本中，或者键入*emoji shortcodes*。

提供一个[表情符号网站](https://emojipedia.org/grinning-face/)

```
:joy:  ———表情短代码
```

:joy:

> 注意：您可以使用此[表情符号简码列表](https://gist.github.com/rxaviers/7360908)，但请记住，表情符号简码因应用程序而异。有关更多信息，请参阅Markdown应用程序的文档。



### 目录(`[toc](name)`)

在文章开头加上`[toc]`可以根据你的标题生成目录

```markdown
[toc] //生成一个目录
```
> 目录的生成本质是根据你的多级标题
> 然而有的解释器要求标题级数必须相邻

### 角标(`^`、`~`)

你可以用`^`包裹来使之成为上角标，用`~`使之成为下角标
```markdown
x^2^ ——上角标
H~2~ ——下角标
```



## Markdown语法速查表



| 元素     | Markdown 语法                                            | 快捷键(Typora)       |
| :------- | -------------------------------------------------------- | -------------------- |
| 标题     | `# H1` <br> `## H2`<br>`### H3`                          | `Ctrl`+`1/2/3/4/5/6` |
| 换行     | `<br>`或结尾两空格+换行符                                | `Enter`              |
| 粗体     | `**bold text**`                                          | `Ctrl`+`B`           |
| 斜体     | `*italicized text*`                                      | `Ctrl`+`I`           |
| 下划线   | `<u>text<\u>`                                            | `Ctrl`+`U`           |
| 删除线   | `~~text~~`                                               |                      |
| 引用     | `> blockquote`                                           | \                    |
| 有序列表 | `1. First item` <br>`2. Second item` <br>`3. Third item` | \                    |
| 无序列表 | `- First item`<br>`* Second item`<br>`+ Third item`      | \                    |
| 任务列表 | `- [ ] text`<br>`- [x] text`                             | \                    |
| 表格   | `\|表头\|表头\|表头\|`<br>`\|:--\|:-:\|--:\|`<br>`\|text\|text\|text\|` | \                   |
| 代码     | \`code\`                                                 |                      |
| 代码块   | \`python<br>print(1)<br>\```                             |                      |
| 分隔线   | `---`                                                    |                      |
| 链接     | `[title](https://www.example.com "desciption")`          |                      |
| 图片     | `![alt text](image.jpg "desciption")`                    |                      |
| 脚注     | `text[^1]`<br>`[^1]`: content                            |                      |
| 角标     | `x^2^`/`H~2~`                                            |                      |
| 目录     | [toc]                                                    |                      |



[^1]: 相关官方教程 https://markdown.com.cn
