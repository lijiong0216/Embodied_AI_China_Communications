# 参考文献逐条出处核查（2026-10-04）

目标稿件：bare_jrnl_new_sample43.tex。核查范围：全部 90 条有效参考文献；末尾 5 条已注释、未在有效正文引用的恢复条目不参与编号，也未改动。

## 结论与修改范围

- 90 条均找到对应的出版机构、官方会议、标准组织、项目官网或 arXiv 原始记录；此次未发现无法对应原始记录的虚构条目。此结论针对书目身份与出版信息，不等同于逐篇复核正文的技术论断或实验结果。
- 修改 46 条书目；正文、图表、标题、引用键和 1–90 的编号顺序均保持不变。
- 按用户偏好，将 10 条未列传统卷页的 ICLR 引用改为 arXiv：MMLU、AgentBench、ReAct、ViT、WebArena、SWE-bench、Habitat 3.0、KVComm、QVLA、DualVLN。年份同步采用 arXiv 初次提交年份，不能保留会议年份冒充预印本年份。
- 补全 6 条 PMLR 卷号：DALL-E 139、Meta-World 100、RT-2 229、Multiagent Debate 235、PaLM-E 202、Speculative Decoding 202。
- Nature 的 Dreamer 3 补 no. 8059；Qwen3 的作者由团队简称对齐 arXiv 著录为 A. Yang et al.；BIG-bench 补官方 OpenReview 入口。
- 为 27 条已经核对身份的正式出版论文补 DOI，便于追溯。未将同名预印本或早期会议版本的元数据套到期刊版本上。

## 为什么仍有条目不含某些字段

1. ICLR 缺少传统卷号/连续页码不能单独证明未录用；本轮改用 arXiv 是遵循用户指定的引用口径，不是否认官方会议记录。arXiv 本身没有期刊卷期与正式连续页码，不填这些字段。
2. BIG-bench 的 TMLR 正式记录和 HumanoidBench 的 RSS 官方 BibTeX 未给出传统卷页组合；分别保留发表年月与官方 URL、会议年月与 DOI，不把 PDF 内页数冒充正式页码。
3. [20] 使用文章编号 121101，不是漏写连续页码。
4. [24]、[25]、[44]、[45]、[54]、[82] 的出版机构登记元数据有卷号和页码，但无期号；保留已确认的卷页，不猜填 no.。
5. 标准、技术报告、项目网页和机构新闻按各自文献类型著录，不适用期刊卷期。网页原访问日 Oct. 1, 2026 保留；本次重新核验日期见本报告。
6. ToDMA、AVERY 和 Action Deviation 保留明确的 v3/v3/v2，年份对应所引版本（2026/2026/2025）；其余无版本后缀的 arXiv 条目使用首次提交年。Q-KVComm 页面给出的初次提交日为 2025-11-27，不从编号月份反推日期。

## 逐条核验记录

期刊的 DOI 元数据来自出版机构向 Crossref 登记的记录；会议卷页优先采用会议官网的 BibTeX/PMLR/ACL/CVF。链接指向对应原始出处。

| 编号 | Citation key | 核验结果及处理 | 原始出处 |
| --- | --- | --- | --- |
| 1 | `nvidiagenai` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://www.nvidia.com/en-us/glossary/generative-ai/) |
| 2 | `gpt3` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) |
| 3 | `dalle` | 补 PMLR vol. 139；已有页码核实 | [官方记录](https://proceedings.mlr.press/v139/ramesh21a.html) |
| 4 | `mmlu` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2009.03300) |
| 5 | `bigbench` | TMLR, May 2023；补官方 URL；不编造卷页 | [官方记录](https://openreview.net/forum?id=uyTL5Bvosj) |
| 6 | `agentbench` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2308.03688) |
| 7 | `react` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2210.03629) |
| 8 | `reflexion` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) |
| 9 | `metaworld` | 补 PMLR vol. 100；已有页码核实 | [官方记录](https://proceedings.mlr.press/v100/yu20a.html) |
| 10 | `rt2` | 补 PMLR vol. 229；已有页码核实 | [官方记录](https://proceedings.mlr.press/v229/zitkovich23a.html) |
| 11 | `libero` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) |
| 12 | `ericssonuplink2026` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/rising-uplink-demand-ai-driven-mobile-networks) |
| 13 | `itu2160` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://www.itu.int/rec/R-REC-M.2160-0-202311-I/en) |
| 14 | `3gpp22870` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=4374) |
| 15 | `hexaxii` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://cordis.europa.eu/project/id/101095759) |
| 16 | `6ggoals` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://cordis.europa.eu/project/id/101139232) |
| 17 | `airan2026` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://ai-ran.org/press-releases/mwc-2026-momentum) |
| 18 | `a2aproject` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents) |
| 19 | `groot` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2503.14734) |
| 20 | `agentsurvey` | vol. 68, no. 2, Art. no. 121101 核实 | [官方记录](https://doi.org/10.1007/s11432-024-4222-0) |
| 21 | `embodiedsurvey` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://doi.org/10.1109/tmech.2025.3574943) |
| 22 | `edgeLLMsurvey` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://doi.org/10.1109/comst.2025.3527641) |
| 23 | `semcomnetsurvey` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://doi.org/10.1109/comst.2024.3516819) |
| 24 | `isea` | 卷页核实；出版元数据无期号，不补写 | [官方记录](https://doi.org/10.1109/comst.2025.3592989) |
| 25 | `semanticclassic` | 卷页核实；出版元数据无期号，不补写；补已验证 DOI | [官方记录](https://doi.org/10.1109/tsp.2021.3071210) |
| 26 | `tokcom` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/mwc.001.2500084) |
| 27 | `bleu` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://aclanthology.org/P02-1040/) |
| 28 | `rouge` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://aclanthology.org/W04-1013/) |
| 29 | `vit` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2010.11929) |
| 30 | `ddpm` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) |
| 31 | `du_debate` | 补 PMLR vol. 235；已有页码核实 | [官方记录](https://proceedings.mlr.press/v235/du24e.html) |
| 32 | `cot` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html) |
| 33 | `tot` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html) |
| 34 | `rag` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) |
| 35 | `agentprotocols` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2505.02279) |
| 36 | `webarena` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2307.13854) |
| 37 | `swebench` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2310.06770) |
| 38 | `palme` | 补 PMLR vol. 202；已有页码核实 | [官方记录](https://proceedings.mlr.press/v202/driess23a.html) |
| 39 | `dreamer3` | 补 no. 8059；vol. 640, pp. 647–653 核实 | [官方记录](https://doi.org/10.1038/s41586-025-08744-2) |
| 40 | `humanoidbench` | RSS 2024；官方 BibTeX 无卷页，保留 DOI | [官方记录](https://doi.org/10.15607/rss.2024.xx.061) |
| 41 | `habitat3` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2310.13724) |
| 42 | `reflexbench` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2608.14379) |
| 43 | `evatok` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.html) |
| 44 | `wdmoe` | 卷页核实；出版元数据无期号，不补写；补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2025.3585163) |
| 45 | `pipeline` | 卷页核实；出版元数据无期号，不补写 | [官方记录](https://doi.org/10.1109/tcomm.2026.3686718) |
| 46 | `progressive` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2022.3221778) |
| 47 | `agentsmobile` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/mwc.2025.3599602) |
| 48 | `estornell` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html) |
| 49 | `thoughtcomm` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b2b502c3629beadda06311386d2c6f73-Abstract-Conference.html) |
| 50 | `latentcomm` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://aclanthology.org/2026.acl-long.1248/) |
| 51 | `hybrid` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/icmlcn64995.2025.11140540) |
| 52 | `todma` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2505.10946v3) |
| 53 | `distributedllm` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jstsp.2025.3581478) |
| 54 | `aircompneural` | 卷页核实；出版元数据无期号，不补写；补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2025.3596344) |
| 55 | `airfusion` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2025.3527331) |
| 56 | `avery` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2511.18151v3) |
| 57 | `specdecode` | 补 PMLR vol. 202；已有页码核实 | [官方记录](https://proceedings.mlr.press/v202/leviathan23a.html) |
| 58 | `actiondeviation` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2510.02851v2) |
| 59 | `qkvcomm` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2512.17914) |
| 60 | `kvcomm` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2510.03346) |
| 61 | `semsharekv` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://doi.org/10.18653/v1/2025.findings-ijcnlp.25) |
| 62 | `garq` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://doi.org/10.1109/iccworkshops63917.2026.11586445) |
| 63 | `flashvla` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2505.21200) |
| 64 | `qvla` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2602.03782) |
| 65 | `dadu` | 补已验证 DOI | [官方记录](https://doi.org/10.1145/3695053.3731099) |
| 66 | `polyanskiy` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/tit.2010.2043769) |
| 67 | `cellfree` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jsac.2023.3280962) |
| 68 | `resourceurlcc` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jsac.2023.3280967) |
| 69 | `interfacediversity` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/tcomm.2017.2771478) |
| 70 | `harq` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jsac.2018.2874122) |
| 71 | `puncturing` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/tnet.2020.2968373) |
| 72 | `ranslicing` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jiot.2021.3068518) |
| 73 | `mobileran` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2021.3060514) |
| 74 | `unifiedqos` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jiot.2025.3567111) |
| 75 | `mixedjitter` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jiot.2025.3566083) |
| 76 | `deterministic` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/tvt.2025.3563916) |
| 77 | `waypoint` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2024.3424493) |
| 78 | `semanticclosedloop` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2512.19177) |
| 79 | `fang` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jsac.2025.3574601) |
| 80 | `pang` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/jsac.2025.3574602) |
| 81 | `systemid` | 补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2023.3314689) |
| 82 | `energywncs` | 卷页核实；出版元数据无期号，不补写；补已验证 DOI | [官方记录](https://doi.org/10.1109/twc.2025.3592969) |
| 83 | `netmcp` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2510.13467) |
| 84 | `qwen3` | arXiv 身份、作者、题名及版本年份核实；作者改为 A. Yang et al. | [官方记录](https://arxiv.org/abs/2505.09388) |
| 85 | `janus` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2410.13848) |
| 86 | `januspro` | arXiv 身份、作者、题名及版本年份核实 | [官方记录](https://arxiv.org/abs/2501.17811) |
| 87 | `dualvln` | 按要求改为 arXiv，同步年份 | [官方记录](https://arxiv.org/abs/2512.08186) |
| 88 | `esl` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://link.springer.com/chapter/10.1007/978-0-387-84858-7_4) |
| 89 | `trafficcnn` | 作者/机构、题名、年份及已有出版字段核实，保留 | [官方记录](https://doi.org/10.1109/isi.2017.8004872) |
| 90 | `bilstm` | 补已验证 DOI | [官方记录](https://doi.org/10.1016/j.neunet.2005.06.042) |

## 验证

- 参考文献之前的 TEX 内容与修改前逐字一致；注释保留区与文件结尾未变。
- 90 个有效书目键与有效正文引用一一对应，无重复、未定义或未引用条目；编号顺序未变。
- 所有改为 arXiv 的条目已核对 ID、题名和作者；未保留不对应的 ICLR 出版年份。
- 三次 pdflatex 编译通过，仍为 16 页；无未定义引用、重复定义或 Overfull 溢出。已渲染并检查第 14–16 页参考文献，未见文本重叠或裁切。
- 正文 TEX 与本轮开始时的源码逐字一致。改前 PDF 与当前 TEX 的正文排版/内容快照并非完全同步，故不宣称新旧 PDF 的正文页提取文本逐字一致；本轮修改范围以已验证的 TEX 差异为准。
- 原稿备份位于：`C:/Users/23880/AppData/Local/Temp/lam-reference-audit-68041c08`。

