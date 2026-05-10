from collections import defaultdict

from core.tokenizer import tokenize
from storage.writer import write_index

from core.structures import doc_len
import core.structures as s


def build_partial_index(docs):

    index = defaultdict(list)

    for docID, text in docs:

        tokens = tokenize(text)
        doc_len[docID] = len(tokens)

        s.N += 1

        tf = defaultdict(int)

        for token in tokens:
            tf[token] += 1

        for term, freq in tf.items():
            index[term].append((docID, freq))

    return index


def process_chunks(all_docs, chunk_size=2):

    chunk_id = 0

    for i in range(0, len(all_docs), chunk_size):

        chunk_docs = all_docs[i:i+chunk_size]

        partial_index = build_partial_index(chunk_docs)

        postings_path = f"data/partial_postings_{chunk_id}.bin"
        lexicon_path = f"data/partial_lexicon_{chunk_id}.pkl"

        write_index(
            partial_index,
            postings_path,
            lexicon_path
        )

        print(f"Chunk {chunk_id} written.")

        chunk_id += 1   

    s.avgdl = sum(doc_len.values()) / s.N