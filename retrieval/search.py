import heapq

from core.tokenizer import tokenize
from core.structures import doc_len

from retrieval.bm25 import bm25_score

from storage.reader import (
    read_postings_from_files
)

def search(
    query,
    postings_path="data/final_postings.bin",
    lexicon_path="data/final_lexicon.pkl",
    top_k=5
):

    query_terms = tokenize(query)

    if not query_terms:
        return []

    postings_map = {}

    for term in query_terms:

        postings = read_postings_from_files(
            term,
            postings_path,
            lexicon_path
        )

        postings_map[term] = postings

    candidate_docs = set()

    for postings in postings_map.values():

        for docID, _ in postings:
            candidate_docs.add(docID)

    scores = []

    for docID in candidate_docs:

        score = bm25_score(
            query_terms,
            postings_map,
            docID,
            doc_len
        )

        scores.append((score, docID))

    return heapq.nlargest(top_k, scores)