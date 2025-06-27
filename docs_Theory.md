# 权重与情绪计算原理 | Weight & Emotion Computation Principles

NovaSeed 系统采用结构化语义驱动的 AI 引擎，不依赖大规模训练，而是通过每个节点的结构角色、频率、情绪与上下文梯度，实现语义推理与反馈。
> NovaSeed is a structural-semantic-driven AI engine. It does not rely on massive training data, but instead reasons through node structure, frequency, emotion, and context gradients.

---

## 🧠 节点权重评分机制 | Node Weight Computation

| 中文字段 | 中文说明 | 英文说明 |
|----------|----------|----------|
| `base_score` | 节点基础分（主语/动作/宾语） | Base score based on node type (subject/action/object) |
| `repeat_bonus` | 频次加成（每多一次+0.05，封顶0.2） | Frequency bonus (+0.05 per occurrence, capped at 0.2) |
| `final_score` | 最终权重 = base + bonus | Final weight = base + bonus |
| `gradient_level` | 权重等级标签（辅助/重要/核心） | Gradient level (support / important / core) |

---

## 🌈 情绪识别与趋势计算 | Emotion Detection & Transition

| 字段 | 中文说明 | 英文说明 |
|------|----------|----------|
| `emotion` | 节点情绪值（正向 / 中性 / 负向） | Node emotional value (Positive / Neutral / Negative) |
| `emotion_transition` | 情绪状态转移（上一句 → 当前句） | Emotional transition from previous to current |
| `trend` | 情绪趋势（趋好 / 趋差 / 趋缓 / 稳定） | Trend: improving / worsening / flattening / stable |

---

## ✅ 输出结构示例 | Example Output

```json
{
  "word": "误诊",
  "type": "action",
  "base_score": 0.9,
  "repeat_bonus": 0.05,
  "final_score": 0.95,
  "emotion": "负向",
  "emotion_en": "Negative",
  "gradient_level": "核心节点",
  "gradient_level_en": "Core node"
}

---

## 🔮 未来扩展规划 | Future Extensions

- 节点联动加权（如“医生”节点引发“误诊”情绪）  
  Node-level emotional linkage (e.g., triggering emotion from related characters)

- 跨句情绪惯性推理（延续性与反转点判断）  
  Cross-sentence emotional inertia modeling (flow and reversal point detection)

- 情绪节奏建模与爆发预测（高潮 / 冷却）  
  Emotional rhythm prediction (build-up and climax estimation)

- 结构权重断裂检测与修复建议（对接 M3）  
  Structural break detection and repair suggestion (integrate with M3 Reasoner)

---

🧠 NovaSeed 强调可解释性与结构溯源，每个权重与情绪变化都能回溯节点与上下文。  
> NovaSeed emphasizes **interpretability and structural traceability** – every weight and emotional shift is tied to logical and contextual structure.


🔍 base_score 判定规则 | Base Score Determination

| 词类型   | base_score | 判定标准                     |
|----------|------------|------------------------------|
| subject  | 0.7        | 命中主语词表，例如“我、她”    |
| action   | 0.9        | 命中动词行为词表，例如“承认”  |
| object   | 0.8        | 命中宾语词表，例如“恐惧”      |
| unknown  | 0.5        | 无法匹配词表，设为默认值       |


> 💬 上述节点中，“承认”被识别为动作词，base_score 为 0.9，重复出现后 final_score 达到 0.95，归为 “核心节点”。
> “自己”被识别为主语，base_score 为 0.7，最终权重为 0.75，归为 “重要节点”。
> 未匹配到词表的词，如“恐惧”，默认 base_score 为 0.5，最终归为 “辅助节点”。

🧠 reasoning_path 推理路径链条 | Reasoning Path Chain
字段名	中文说明	英文说明
reasoning_path	从上下文中构建出的语义推理路径链，如“因 → 果”、“假设 → 结果”、“情绪 → 行动”	
Semantic reasoning path derived from context, such as 
"cause → effect", "hypothesis → consequence", "emotion → action"

 emotion\_curve  模拟情绪曲线走势（如上升、下跌、稳定）用于情绪动画和节奏节点评估 
 Simulated emotional trend curve (e.g., rising, falling, stable), used for animation rhythm and emotional pacing 


emotion\_curve | 模拟情绪曲线走势（如上升、下跌、稳定）用于情绪动画和节奏节点评估 
Simulated emotional trend curve (e.g., rising, falling, stable), 
used for animation rhythm and emotional pacing 

json:
"questions": [
  "她为什么恐惧？",
  "真相是什么？",
  "是谁让她看见真相的？"
]


