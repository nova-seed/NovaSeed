🌱 NovaSeed Architecture | NovaSeed 架构说明
🧠 Overview | 概述
NovaSeed is a modular structural AI engine designed for 
explainable understanding and reasoning.

NovaSeed 是一个模块化结构化 AI 引擎，专为可解释的语义理解与推理而设计。
Unlike traditional large models that rely on probabilistic prediction, NovaSeed builds semantic comprehension through structured nodes,
 relationships, and gradient weights.
与依赖概率预测的大模型不同，NovaSeed 通过结构化节点、关系链与权重梯度构建语义理解过程。




🔁 Processing Flow | 处理流程总览
input.txt
   ↓
[M1] Input Router → [M2] Node Classifier → [M3] Path Reasoner → [M4] Emotion Engine → [M5] QA Generator
   ↓
[M6] Visual Renderer（可选） → [M7] File Transit（可选） → [M8] User Interactor（可选）
   ↓
[M9] Controller

Each module handles one semantic dimension and forms a chain reaction.
每个模块处理一种语义维度，形成联动闭环。

| ID | Module          | Description (EN)                                           | 描述（中文）                  |
| -- | --------------- | ---------------------------------------------------------- | ----------------------- |
| M1 | Input Router    | Sentence splitting, tokenization, basic node detection     | 分句、分词、初级节点（主语/动作/客体）识别  |
| M2 | Node Classifier | Fine-grained tagging of node types using expanded ontology | 使用本体词典进行细分类标注，提升节点识别精度  |
| M3 | Path Reasoner   | Identify logical breaks and suggest completions            | 判断语义链断裂，自动生成修复建议与替代路径   |
| M4 | Emotion Engine  | Evaluate emotion weight, polarity, and emotional curves    | 分析情绪权重、极性、情绪曲线与转换趋势     |
| M5 | QA Generator    | Generate context-aware follow-up or reflective questions   | 生成基于当前语境的追问、反问或补充问题     |
| M6 | Visual Renderer | Convert output into animated text or story frame visuals   | 将结构化输出转换为动画帧、场景画面（可选模块） |
| M7 | File Transit    | Handle compressed data transfer without manual path input  | 无需文件路径的压缩+传输系统，支持自动格式解析 |
| M8 | User Interactor | Manage dialogue, secondary questions, and input feedback   | 管理交互式对话、二级提问与内容反馈（可选模块） |
| M9 | Controller      | Orchestrate module scheduling and global task logic        | 调度各模块调用顺序，执行全局控制与任务路径   |


📥 Input/Output Schema | 输入输出字段规范
每个模块都有明确的输入与输出字段，保证结构通用性与可扩展性。

🔹 M1: Input Router 输入输出格式
输入（input.txt）：
她看见了真相，决定承认自己内心的恐惧。

输出（m1_output.json）：
[
  {
    "sentence": "她看见了真相，决定承认自己内心的恐惧。",
    "tokens": ["她", "看见", "了", "真相", "决定", "承认", "自己", "内心", "的", "恐惧"],
    "nodes": [
      {
        "word": "承认",
        "type": "action",
        "emotion": "正向",
        "base_score": 0.9,
        "repeat_bonus": 0.05,
        "final_score": 0.95,
        "gradient_level": "核心节点"
      },
      {
        "word": "自己",
        "type": "subject",
        "emotion": "中性",
        "final_score": 0.75,
        "gradient_level": "重要节点"
      }
    ],
    "emotion_transition": {
      "from": "中性",
      "current": "正向",
      "trend": "趋好"
    }
  }
]


🔄 Data Flow Across Modules | 模块数据流动说明
来源模块	输出字段（字段名）	接收模块	用途说明
M1	nodes[].type	M2	进行节点二次精细分类
M1	emotion_transition.current	M4	用于分析情绪趋势与转折
M2	type:subject/action/object	M3	构建语义链路径
M3	reasoning_path	M5	用于生成相关联的问题链
M4	emotion_curve	M6	动画中用于驱动人物情绪波动
M5	questions[]	M8	用户提示与交互式反馈

🔮 Future Roadmap | 后续扩展规划
项目	状态	描述
多语言支持	✅ 已支持中文	未来将引入英文、西语等分词器
模块异步并行执行	🚧 进行中	支持 M2~M5 并行运行，提高处理效率
可视化结构输出	🔜 规划中	使用 SVG/WebGL 生成节点图与情绪热力图
结构节点图谱持久化（Neo4j）	🔜 规划中	输出可回溯的知识图谱与行为流，用于长期推理
---

---
### 📌 System Field Reference

| Field                        | Description                                     | Origin Module |
|-----------------------------|-------------------------------------------------|---------------|
| nodes[].type                | Node type classification (subject/action/object)| M1            |
| emotion_transition.current  | Dominant emotional status                       | M4            |
| reasoning_path              | Chain of reasoning context                      | M5            |
| emotion_curve               | Emotion gradient score (used for animation)     | M4            |
| questions[]                 | Follow-up Q&A generated from context            | M6            |



