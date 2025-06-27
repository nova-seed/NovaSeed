import os
import json
import jieba
from collections import defaultdict

# ========= 配置关键词 =========
SUBJECT_WORDS = ["医生", "病人", "她", "他", "你", "自己"]
ACTION_WORDS = ["误诊", "咳嗽", "承认", "决定", "看见", "异化", "说", "继续"]
OBJECT_WORDS = ["真相", "恐惧", "懦弱", "疽虫"]

# ========= 节点分类 =========
def classify_node_type(word):
    if word in SUBJECT_WORDS:
        return "subject"
    elif word in ACTION_WORDS:
        return "action"
    elif word in OBJECT_WORDS:
        return "object"
    else:
        return "unknown"

# ========= 情绪判定 =========
def detect_emotion(word):
    # 可拓展的关键词情绪字典
    if word in ["恐惧", "懦弱"]:
        return "负向"
    elif word in ["真相", "承认"]:
        return "正向"
    else:
        return "中性"

# ========= 权重计算 =========
def compute_weight(word, freq_count):
    type_ = classify_node_type(word)
    base = {"subject": 0.7, "action": 0.9, "object": 0.8}.get(type_, 0.5)
    bonus = min(0.05 * freq_count[word], 0.2)
    return base, bonus, round(base + bonus, 2)

# ========= 情绪趋势判断 =========
def get_dominant_emotion(emotions):
    scores = {"负向": -1, "中性": 0, "正向": 1}
    total = sum([scores.get(e, 0) for e in emotions])
    if total > 0:
        return "正向"
    elif total < 0:
        return "负向"
    else:
        return "中性"

def get_emotion_trend(previous, current):
    levels = {"负向": -1, "中性": 0, "正向": 1}
    if previous is None:
        return "稳定"
    delta = levels[current] - levels[previous]
    return "趋好" if delta > 0 else "趋差" if delta < 0 else "趋缓"

# ========= 主分析函数 =========
def analyze_sentences(text):
    sentences = text.strip().split("。")
    freq_count = defaultdict(int)
    for sent in sentences:
        for token in jieba.cut(sent):
            freq_count[token] += 1

    results = []
    prev_emotion = None

    for sent in sentences:
        if not sent.strip():
            continue

        tokens = list(jieba.cut(sent))
        nodes = []
        emotions = []

        for word in tokens:
            node_type = classify_node_type(word)
            emotion = detect_emotion(word)
            base, bonus, final = compute_weight(word, freq_count)
            level = "观察节点"
            if final >= 0.9:
                level = "核心节点"
            elif final >= 0.7:
                level = "重要节点"
            elif final >= 0.5:
                level = "辅助节点"

            nodes.append({
                "word": word,
                "type": node_type,
                "emotion": emotion,
                "base_score": base,
                "repeat_bonus": round(bonus, 2),
                "final_score": final,
                "gradient_level": level
            })
            emotions.append(emotion)

        dominant_emotion = get_dominant_emotion(emotions)
        trend = get_emotion_trend(prev_emotion, dominant_emotion)

        results.append({
            "sentence": sent + "。",
            "tokens": tokens,
            "nodes": nodes,
            "emotion_transition": {
                "from": prev_emotion,
                "current": dominant_emotion,
                "trend": trend
            }
        })
        prev_emotion = dominant_emotion

    return results

# ========= 主入口 =========
if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))  # 切换当前目录
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()
    print("读取到的文本：", text)

    output = analyze_sentences(text)

    if output:
        with open("m1_output.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print("✅ M1模块处理完成，结果保存为 m1_output.json")
    else:
        print("⚠️ 分析结果为空，未写入文件")

