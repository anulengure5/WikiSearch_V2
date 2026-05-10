import math
from core.structures import index, df, doc_len
import core.structures as s
from config import K1, B

def bm25_score(query_terms, postings_map, docID, doc_len):

    score = 0.0

    for term in query_terms:

        if term not in postings_map:
            continue

        postings = postings_map[term]

        df_t = len(postings)

        idf = math.log(
            (s.N - df_t + 0.5) / (df_t + 0.5) + 1
        )

        tf = 0

        for d, freq in postings:
            if d == docID:
                tf = freq
                break

        if tf == 0:
            continue

        denom = tf + K1 * (
            1 - B + B * (doc_len[docID] / s.avgdl)
        )

        score += idf * (
            (tf * (K1 + 1)) / denom
        )

    return score