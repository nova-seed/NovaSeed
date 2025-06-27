
# 🛰️ NovaSeed v0.1 – Reasoning Seed Takes Root

> **“Not a chatbot. A seed of reasoning.”**

NovaSeed is a modular semantic AI engine focused on structural understanding and emotional explainability.  
It builds meaning not from brute-force data but from node structure, scoring, and context transitions.

---

## 🚀 What's Included in v0.1

**✅ Core Module Implemented:**
- `M1 Input Router`  
  - Sentence segmentation, tokenization  
  - Node classification (subject/action/object/unknown)  
  - Token emotion tagging (positive/neutral/negative)  
  - Node weight scoring (`base_score`, `repeat_bonus`, `final_score`)  
  - Emotion trend tracking (`transition`, `trend`)  
  - Output to `m1_output.json`

**✅ Documentation:**
- `README.md` – Project overview, module guide, usage instructions (中英文双语)
- `docs_Architecture.md` – System design, data flow, and module logic
- `docs_Theory.md` – Weight & emotion scoring, reasoning rules, examples

---

## 📂 Sample Files

| File | Description |
|------|-------------|
| `input.txt` | Example input text (中文情感语句) |
| `m1_output.json` | Structured semantic output with token + emotion + reasoning trace |

---

## 📌 Vision

> NovaSeed is **not a chatbot.**  
> It’s a modular, reasoning-first AI system aiming to restore explainability to language understanding.

This is only the beginning.  
Future versions will include:

- `M2–M9` full pipeline (reasoning, emotion engine, Q&A, rendering…)
- SVG/WebGL-based node animation
- Neo4j memory graph integration
- Multi-language support (中文 / English)
- GPT/Claude plugin compatibility

---

## 🔧 How to Run Locally

```bash
python input_router.py
```

**Input:** `input.txt`  
**Output:** `m1_output.json` with structured semantic/emotional trace

---

## 🙌 Join Us

If you're tired of black-box AI and believe in structure-first intelligence — NovaSeed is your open-source ground zero.
