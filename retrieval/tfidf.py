import math
from core.structures import index, df, N

def tfidf_score(query_terms, docID):
    score = 0.0

    for term in query_terms:
        if term not in index:
            continue

        idf = math.log((N + 1) / (df[term] + 1))

        for d, tf in index[term]:
            if d == docID:
                score += tf * idf

    return score