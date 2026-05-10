from utils.loader import load_docs
from core.indexer import build_index
from retrieval.search import search
from storage.writer import write_index
from storage.partial_writer import process_chunks
from storage.merger import merge_indexes


def main():
    docs = load_docs()
    process_chunks(docs, chunk_size=2)

    merge_indexes()

    while True:
        query = input("Enter query: ")
        if query.strip() == "exit":
            break

        results = search(query)
        
        if not results:
            print("No results found.")
        else:
            for score, docID in results:
             print(f"Doc {docID} → Score: {score:.4f}")
        

if __name__ == "__main__":
    main()


import pickle

with open("data/lexicon.pkl", "rb") as f:
    lexicon = pickle.load(f)

print(lexicon)



