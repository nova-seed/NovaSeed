# 🌐 M2 Module | Emotion Evaluator 情绪评分器模块

# 📌
OverThe Emotion Evaluator (M2) is a structured emotion scoring engine based on five dynamic factors, supporting NovaSeed’s cognition system.

## 🔍 Usage Scenarios | 应用场景示例
- Detecting hidden emotional complaints in daily conversation.
- Supporting dynamic emotional routing in dialogue systems.
- Preprocessing for deeper reasoning (e.g., M5 conflict analysis).


1. **Frequency** – Measures how often emotionally suggestive expressions appear (e.g., “你自己”, “体会”).
2. **Intensity** – Indicates hidden emotional force such as suppression, sarcasm, or passive aggression.
3. **Triggering Context** – Detects whether unresolved issues or triggers are referenced.
4. **Continuity** – Identifies repeated patterns showing long-term buildup (e.g., “每次”, “总是”).
5. **Subjectivity** – Recognizes personal emotional anchoring (e.g., “我觉得你…”).


---

#  中文说明
M2 模块负责将输入句子的情绪结构进行识别与浮动评分，评分机制基于五大核心因子：
1. **频率**：是否包含带有情绪提示的表达，如“你自己”、“体会”、“吧”等。
2. **强度**：是否存在情绪压抑、冷淡、讽刺等非直接表达。
3. **触发事件**：是否提及未解决问题或情绪上下文背景。
4. **持续性**：出现“每次”、“总是”、“一直”等，表明情绪积压。
5. **主客观**：是否使用“我觉得你…”等主观视角，说明自我受伤或委屈感。

系统将基于以上五因子计算情绪波动路径，并输出结构化评分结果与跳转建议（如跳入 M5 模块进行差异链分析）。


---

## 📤 Input Format

````json

{
  "original_text": "你自己好好体会吧。",
  "context": "...(optional)..."
}


{
  {
  "original_text": "你自己好好体会吧。",
  "emotion_type": "negative",
  "score": -0.42,
  "pre_emotion_flag": true,
  "sensitivity_index": 0.63,
  "suggested_jump": "M5",
  "emotion_path": ["期待", "委屈", "冷嘲"],
  "node_structure": {
    "subject": "你",
    "action": "体会"
  }
}

}


🔒 Note on Algorithm Protection

The formulas and weight distributions used in this module are proprietary and confidential.
This document focuses only on the structural explanation of inputs and outputs. No internal algorithmic logic is disclosed.

🔒 算法保护说明

M2 模块的情绪评分核心算法与权重逻辑为保密机制，不在此文档中公开。本说明仅面向输入/输出结构与评分解释部分。
