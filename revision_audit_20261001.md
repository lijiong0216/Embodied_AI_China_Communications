# 本轮修改与参考文献核查记录

核查日期：2026-10-01。目标文件：`bare_jrnl_new_sample43.tex`。
意见来源：`overleaf_comments_Embodied_AI_China_Communications_2026-09-30T17-09-48-423Z.json`。

## 修改范围

仅处理该 JSON 中 4 条未解决意见，以及本轮另行要求的参考文献和页眉。已解决意见不重新展开；原有注释掉的正文、实验数据、作者和基金信息均保留。

| 意见 | 处理 |
| --- | --- |
| 无来源的 token-value 指标 | 删除自拟的 `s_k(t)` 公式及依赖该公式的推断；用 FlashVLA、QVLA 和 DaDu-Corki 的具体机制替代，并将闭环损失理论列为待研究问题。 |
| 更新 Introduction、保持组织方式和主要内容 | 保持原有小节结构和四项贡献，更新流量特征、场景化 QoS 以及实测/提议两阶段的边界。 |
| 更新摘要 | 对齐全文与实际实验：2,300 个独立处理的 10-s 片段、460 个测试片段、99.83–100% Macro-F1；不把待验证的主动识别方案写成实验成果。 |
| 更新路线图 | 编辑原有 PPTX 原生文本/形状，按当前有效章节删除过时小节，更新两阶段 case study 和未来方向，导出新版 PDF。 |

页眉恢复为项目中 `New_IEEEtran_how-to.tex` 的原始示例文字：

```latex
Journal of \LaTeX\ Class Files,~Vol.~18, No.~9, September~2020
```

这是 IEEE 模板占位页眉，并非声称本文已在该刊期发表。作者侧页眉保持原状。

## 文献核查结论与边界

- 原参考文献表 86 条；当前有效正文引用 81 条。为 `vllm`、`multitier`、`edgeinference`、`offloading`、`rifl` 保留注释形式的条目，不再编入有效参考文献表。其中后四条的正文引用也处于注释中。
- 81 条有效条目均找到相应的出版机构、官方会议记录、作者机构仓储、标准组织或 arXiv 原始记录。此次未发现可确认的虚构条目。
- 核查覆盖条目身份、可获取的作者/题名/出版信息、引用位置及重点方法归因；不等同于逐篇复现实验，也不能保证所有文献结论本身正确。
- 按有效正文首次引用顺序重排，保留原 citation keys；统一作者省略方式、会议/期刊缩写、页码和日期。作者不超过 6 位时列全，超过 6 位时采用首位作者加 et al.，依据 [IEEE Reference Guide](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE_Reference_Guide.pdf)。
- 修正两处引用范围过宽：GARQ 仅归因于异构边缘 LLM 的自适应重复查询，不再归因于未经核实的“latent concept”机制；技术映射表中 NetMCP/GARQ 仅支撑网络感知工具路由与重复查询，不再支撑最小辩论图或 rollback。

### 主要书目信息修正

| citation key | 修正 |
| --- | --- |
| `3gpp22870` | 补充 TR 22.870 v20.0.0、Release 20、2026 年 3 月。 |
| `bigbench` | 将笼统 BIG-bench Authors 改为 A. Srivastava et al.。 |
| `isea` | 将 early access 更新为 COMST vol. 28, pp. 2725–2770, 2026，并补 DOI。 |
| `du_debate` | 使用 ICML 2024 正式版本和页码。 |
| `dreamer3` | 使用 Nature 2025 正式题名、卷页和 DOI。 |
| `groot` | 使用首位个人作者 J. Bjorck et al.，替代 NVIDIA et al.。 |
| `humanoidbench` | 使用 RSS 2024 正式会议记录和 DOI。 |
| `evatok` | 使用 CVPR 2026 正式会议页码。 |
| `edgeLLMsurvey` | 补全期号和月份。 |
| `pipeline` | 将 early access 更新为 TCOM vol. 74, pp. 8390–8406, 2026，并补 DOI。 |
| `agentprotocols` | 恢复四个协议全称，避免缩写替代原题名。 |
| `thoughtcomm` | 使用 NeurIPS 2025 正式卷页。 |
| `todma` | 对齐 arXiv v3 的新题名和 2026 年 7 月版本日期。 |
| `avery`, `actiondeviation` | 显式标出 v3/v2，使日期与所引版本一致。 |
| `semsharekv` | 标明 Findings 文集和 DOI，避免与主会混淆。 |
| `qvla` | 使用 ICLR 2026 正式会议版本。 |
| `tot`, `reflexion`, `libero`, `estornell` | 补齐官方 proceedings 页码。 |
| `trafficcnn` | 补齐 5 位作者。 |

保留了核实后确属原题名的 `Principals`（Estornell）与 `convolution neural networks`（Wang）；没有按语言习惯擅自改成另一个题名。Q-KVComm 的 arXiv 页面明确给出 2025 年 11 月提交日期，未仅凭编号月份更改。

## 有效文献的核验入口

以下使用稳定 citation key，而非重排前后的数字编号。DOI 入口对应出版机构登记的书目；会议/arXiv 入口对应正式 proceedings 或作者上传记录。

| Key | 原始记录 / 核验入口 |
| --- | --- |
| `nvidiagenai` | [NVIDIA](https://www.nvidia.com/en-us/glossary/generative-ai/) |
| `3gpp22870` | [3GPP specification record](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=4374) |
| `gpt3` | [NeurIPS 2020](https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) |
| `dalle` | [ICML 2021](https://proceedings.mlr.press/v139/ramesh21a.html) |
| `mmlu` | [ICLR 2021](https://openreview.net/pdf?id=d7KBjmI3GmQ) |
| `bigbench` | [Author-hosted TMLR paper](https://joshrule.com/files/srivastava2023beyond.pdf) |
| `agentbench` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html) |
| `react` | [Author record / ICLR 2023](https://arxiv.org/abs/2210.03629) |
| `reflexion` | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) |
| `metaworld` | [CoRL proceedings](https://proceedings.mlr.press/v100/yu20a.html) |
| `rt2` | [CoRL proceedings](https://proceedings.mlr.press/v229/zitkovich23a.html) |
| `libero` | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) |
| `edgeLLMsurvey` | [IEEE DOI](https://doi.org/10.1109/COMST.2025.3527641) |
| `semanticclassic` | [Author institution](https://qmro.qmul.ac.uk/xmlui/handle/123456789/71804) |
| `tokcom` | [IEEE Xplore](https://ieeexplore.ieee.org/document/11175596/) |
| `isea` | [IEEE DOI](https://doi.org/10.1109/COMST.2025.3592989) |
| `bleu` | [ACL Anthology](https://aclanthology.org/P02-1040/) |
| `rouge` | [ACL Anthology](https://aclanthology.org/W04-1013/) |
| `vit` | [ICLR 2021](https://openreview.net/pdf?id=YicbFdNTTy) |
| `ddpm` | [NeurIPS 2020](https://papers.nips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) |
| `du_debate` | [ICML 2024](https://proceedings.mlr.press/v235/du24e.html) |
| `cot` | [NeurIPS 2022](https://proceedings.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html) |
| `tot` | [NeurIPS 2023](https://proceedings.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html) |
| `rag` | [NeurIPS 2020](https://papers.nips.cc/paper_files/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) |
| `agentprotocols` | [arXiv](https://arxiv.org/abs/2505.02279) |
| `webarena` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4410c0711e9154a7a2d26f9b3816d1ef-Abstract-Conference.html) |
| `swebench` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html) |
| `palme` | [ICML 2023](https://proceedings.mlr.press/v202/driess23a.html) |
| `dreamer3` | [Nature](https://www.nature.com/articles/s41586-025-08744-2) |
| `groot` | [arXiv](https://arxiv.org/abs/2503.14734) |
| `humanoidbench` | [RSS 2024](https://www.roboticsproceedings.org/rss20/p061.html) |
| `habitat3` | [ICLR 2024](https://openreview.net/pdf?id=4znwzG92CE) |
| `reflexbench` | [arXiv](https://arxiv.org/abs/2608.14379) |
| `evatok` | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.html) |
| `wdmoe` | [IEEE DOI](https://doi.org/10.1109/TWC.2025.3585163) |
| `pipeline` | [IEEE DOI](https://doi.org/10.1109/TCOMM.2026.3686718) |
| `progressive` | [Author institution](https://spiral.imperial.ac.uk/entities/publication/ed038593-31d8-4942-b8cf-ee15080d60e0) |
| `agentsmobile` | [IEEE DOI](https://doi.org/10.1109/MWC.2025.3599602) |
| `estornell` | [NeurIPS 2024](https://papers.nips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html) |
| `thoughtcomm` | [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b2b502c3629beadda06311386d2c6f73-Abstract-Conference.html) |
| `latentcomm` | [ACL Anthology](https://aclanthology.org/2026.acl-long.1248/) |
| `hybrid` | [IEEE DOI](https://doi.org/10.1109/ICMLCN64995.2025.11140540) |
| `todma` | [arXiv v3](https://arxiv.org/abs/2505.10946v3) |
| `distributedllm` | [IEEE DOI](https://doi.org/10.1109/JSTSP.2025.3581478) |
| `aircompneural` | [IEEE DOI](https://doi.org/10.1109/TWC.2025.3596344) |
| `airfusion` | [IEEE DOI](https://doi.org/10.1109/TWC.2025.3527331) |
| `avery` | [arXiv v3](https://arxiv.org/abs/2511.18151v3) |
| `specdecode` | [ICML 2023](https://proceedings.mlr.press/v202/leviathan23a.html) |
| `actiondeviation` | [arXiv v2](https://arxiv.org/abs/2510.02851v2) |
| `qkvcomm` | [arXiv](https://arxiv.org/abs/2512.17914) |
| `kvcomm` | [Author record / ICLR 2026](https://arxiv.org/abs/2510.03346) |
| `semsharekv` | [ACL Anthology](https://aclanthology.org/2025.findings-ijcnlp.25/) |
| `garq` | [IEEE DOI](https://doi.org/10.1109/ICCWorkshops63917.2026.11586445) |
| `flashvla` | [arXiv](https://arxiv.org/abs/2505.21200) |
| `qvla` | [ICLR 2026](https://openreview.net/pdf?id=TpL2nXanru) |
| `dadu` | [ISCA DOI](https://doi.org/10.1145/3695053.3731099) |
| `polyanskiy` | [IEEE DOI](https://doi.org/10.1109/TIT.2010.2043769) |
| `cellfree` | [IEEE DOI](https://doi.org/10.1109/JSAC.2023.3280962) |
| `resourceurlcc` | [IEEE DOI](https://doi.org/10.1109/JSAC.2023.3280967) |
| `interfacediversity` | [IEEE DOI](https://doi.org/10.1109/TCOMM.2017.2771478) |
| `harq` | [Author-hosted paper](https://users.ece.utexas.edu/~gustavo/papers/AnD18j.pdf) |
| `puncturing` | [IEEE DOI](https://doi.org/10.1109/TNET.2020.2968373) |
| `ranslicing` | [IEEE DOI](https://doi.org/10.1109/JIOT.2021.3068518) |
| `mobileran` | [IEEE Xplore](https://ieeexplore.ieee.org/document/9364885/) |
| `unifiedqos` | [IEEE DOI](https://doi.org/10.1109/JIOT.2025.3567111) |
| `mixedjitter` | [IEEE DOI](https://doi.org/10.1109/JIOT.2025.3566083) |
| `deterministic` | [IEEE DOI](https://doi.org/10.1109/TVT.2025.3563916) |
| `waypoint` | [Author institution](https://kclpure.kcl.ac.uk/portal/en/publications/goal-oriented-semantic-communications-for-robotic-waypoint-transm/) |
| `semanticclosedloop` | [arXiv](https://arxiv.org/abs/2512.19177) |
| `fang` | [IEEE ComSoc October 2025 contents](https://www.comsoc.org/system/files/2025-11/publications_contents_digest_2025_oct.pdf) |
| `pang` | [IEEE ComSoc October 2025 contents](https://www.comsoc.org/system/files/2025-11/publications_contents_digest_2025_oct.pdf) |
| `systemid` | [IEEE ComSoc May 2024 contents](https://www.comsoc.org/system/files/2024-06/Publications_Contents_Digest_2024_May.pdf) |
| `energywncs` | [IEEE DOI](https://doi.org/10.1109/TWC.2025.3592969) |
| `netmcp` | [arXiv](https://arxiv.org/abs/2510.13467) |
| `qwen3` | [arXiv](https://arxiv.org/abs/2505.09388) |
| `janus` | [arXiv](https://arxiv.org/abs/2410.13848) |
| `januspro` | [arXiv](https://arxiv.org/abs/2501.17811) |
| `dualvln` | [ICLR 2026 paper](https://openreview.net/pdf/1a25efebc28583e7d38570ab67050516fcc20d8e.pdf) |
| `esl` | [Authors' book site](https://hastie.su.domains/ElemStatLearn/) |
| `trafficcnn` | [IEEE DOI](https://doi.org/10.1109/ISI.2017.8004872) |
| `bilstm` | [Publisher DOI](https://doi.org/10.1016/j.neunet.2005.06.042) |

## 编译与交付检查

- 连续三次 pdflatex 编译通过；当前双栏 15 页。未为追求旧版页数要求压缩或改写本轮未授权区域。
- 有效引用和书目键一一对应；无未定义引用/交叉引用、重复标签、LaTeX 错误或 Overfull 溢出。
- 仍有 IEEEtran 的浮动位置自动调整和 Underfull 排版提示，主要来自原有窄表格与双栏断行。未据此改动无意见区域的布局。
- 已逐页查看编译 PDF，并核对路线图 PDF；新版 PPTX 保留可编辑文本与形状，完成结构验证和 PowerPoint 原生导出验证。
- 改前 TEX/PPTX/路线图 PDF 和稿件 PDF 已留在备份目录：`C:/Users/23880/AppData/Local/Temp/lam-revision-20261001-960cd823/`。
