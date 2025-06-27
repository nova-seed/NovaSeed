# 🌱 NovaSeed v0.1 发布说明

NovaSeed 是一个模块化结构驱动的 AI 系统，通过结构语义构建完整的理解链路。该版本是 NovaSeed 的最小可运行结构版本，具备基础语义节点识别、情绪评分、结构导出等核心功能。

---

## ✅ 当前版本亮点

- 输入路由器：自动分句、打分、识别情绪（input_router.py）
- 词语结构识别：自动标注词语类型（subject / action / object）
- 情绪曲线模拟：记录情绪主趋势（中性 → 正向等）
- 节奏层级评估：输出 final_score 与结构级别（辅助/重要/核心）
- 自动输出 JSON：包含 token、node、emotion_transition、结构层级等

---

## 📁 核心模块

| 模块 | 功能 |
|------|------|
| M1 Input Router | 分句、打分、情绪标注 |
| M2 Node Classifier | 节点分类（主语/动作/宾语） |
| M4 Emotion Engine | 情绪识别与趋势曲线 |
| M5 Path Reasoner | 结构路径识别（预留） |
| M6 QA Generator | 上下文追问生成（预留） |

---

## 🔧 如何运行

```bash
python input_router.py
```

输入文件：`input.txt`  
输出文件：`m1_output.json`

---

## 🔮 愿景

NovaSeed 的目标是打造一颗「结构化推理种子」，摆脱大模型纯训练依赖，通过模块化结构表达，赋予 AI 可解释性与情绪理解能力。

> 不止是聊天，它是理解的开始。

---

## 📍 后续路线（规划）

- [ ] M2-M5 模块连贯执行
- [ ] 节奏动画输出（SVG/WebGL）
- [ ] QA 模块生成上下文问题
- [ ] 结构图谱可视化（Neo4j）