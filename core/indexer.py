from collections import defaultdict
from core.tokenizer import tokenize
from core.structures import index, df, doc_len
import core.structures as s

def build_index(docs):
    """
    docs: list of (docID, text)
    """
    for docID, text in docs:
        tokens = tokenize(text)
        doc_len[docID] = len(tokens)

        tf = defaultdict(int)
        for token in tokens:
            tf[token] += 1

        for term, freq in tf.items():
            index[term].append((docID, freq))
            df[term] += 1

    s.N = len(docs)
    s.avgdl = sum(doc_len.values()) / s.N if s.N > 0 else 0