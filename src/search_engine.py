import re
from rank_bm25 import BM25Okapi
from rapidfuzz import process, fuzz

SCORE_THRESHOLD = 0


def tokenize(text: str) -> list:
    return re.sub(r"[^\w\s]", " ", text.lower()).split()


def nlp_search(term: str, commands: dict, top_k: int = 15) -> list:
    documents = []
    for topic, cmds in commands.items():
        for c in cmds:
            documents.append({
                **c,
                "topic": topic,
                "tokens": tokenize(f"{c['cmd']} {c['desc']} {topic}")
            })

    bm25 = BM25Okapi([d["tokens"] for d in documents])

    vocab = {tok for d in documents for tok in d["tokens"]}

    corrected = []
    for tok in tokenize(term):
        match = process.extractOne(tok, vocab, scorer=fuzz.ratio, score_cutoff=70)
        corrected.append(match[0] if match else tok)

    scores = bm25.get_scores(corrected)
    ranked = sorted(
        [(documents[i], scores[i]) for i in range(len(documents)) if scores[i] > SCORE_THRESHOLD],
        key=lambda x: x[1],
        reverse=True
    )[:top_k]

    return [r[0] for r in ranked]
