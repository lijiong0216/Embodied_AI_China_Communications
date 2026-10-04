# China Communications 投稿文件拆分

## 已生成文件

- `../output/pdf/China_Communications_Main_Document.pdf`：16 页匿名主文档，在投稿系统中选择 **Main Document (PDF Preferred)**。
- `../output/pdf/China_Communications_Title_Page.pdf`：1 页作者信息页，在投稿系统中选择 **Title Page**。

这是基于现有稿件的匿名拆分版，不是已经完成所有官方模板要求及作者材料的最终投稿套件。

## 本次处理范围

- 原始 `bare_jrnl_new_sample43.tex` 和同名 PDF 均未覆盖。
- 从主文档删除作者、IEEE 会员身份、单位、通讯作者信息和基金致谢；这些已有信息集中到 Title Page。
- 去掉主文档的示例期刊页眉与作者页眉，保留连续页码。
- 主文档 PDF 的 Author 元数据为空，不嵌入源文件路径或附件。
- 论文题目、摘要、关键词、正文、图表和 90 条有效参考文献均保留；从 `\begin{abstract}` 至文档末尾的源文本与原稿一致。
- Title Page 中作者顺序、单位对应关系、通讯作者和四个基金编号全部取自原稿；未编造邮箱、作者简介、签名、收稿日期、出版日期或编辑信息。

## 上传前仍需补齐／确认

1. **通讯邮箱**：指南第 4.2 节要求提供通讯作者邮箱，原稿未提供。请在 `title_page_data.json` 的 `corresponding_email` 字段填写本次投稿使用的邮箱并重新生成 Title Page。
2. **作者简介和照片**：指南第 XII 节要求作者简介；目前原稿没有六位作者的真实简介及配套照片。本次未添加虚构内容。匿名主文档中不要放作者简介；作者材料应放入非匿名 Title Page 或按编辑部要求另附。
3. **官方模板**：指南介绍的是 `ccjnl.cls`，当前项目只有 `IEEEtran.cls`，未取得可核验的配套官方模板。因此主文档保留现有 IEEEtran 双栏版式，未声称已经转换为官方 China Communications 模板。指南的 `gbt7714-numerical` 参考文献格式也未在本次拆分中转换；保留已经核验的原稿参考文献。
4. **源文件／图片要求**：指南列出 `.tex`、`.cls`、`.bib`、`.log`、`.bbl` 及至少 200 dpi 的 EPS 图片要求。当前生成的是截图要求的两个 PDF，不是用于后续生产排版的完整源文件包；现有 PDF/PNG 图未转换为 EPS。
5. **Author Commitment Statement**：截图要求单独上传。本次未生成或代签该声明，应使用投稿系统提供的官方表格，由作者确认并完成。

## 本地复现

在工作区运行 `submission/build_submission.ps1` 可重新生成两份 PDF。Title Page 的可编辑信息位于 `title_page_data.json`，其排版程序为 `create_title_page.py`。匿名主文档源文件为 `China_Communications_Main_Document.tex`，仍使用项目根目录的类文件和图片。

`check_submission.py` 执行正文一致性、作者信息分离、基金编号、PDF 元数据、页数和附件检查。编译及可视化检查中间文件位于 `tmp/pdfs/submission/`，不要上传。

## 检查结果

- 主文档 16 页，作者信息页 1 页，均已渲染检查。
- 无 LaTeX 编译错误、未定义引用或 Overfull 排版警告；仅有 `h` 浮动体位置自动扩展为 `ht` 的提示。
- 原稿 SHA-256：`4bb925f096a567dcb7c042d6cb449bbb75eadb9a6c990617aae2d7a47e1e49cd`，处理后未变化。
- 主文档无作者全名、所属学校、基金编号、示例期刊页眉或作者元数据；合法的第三人称文献署名不作匿名化删除。
