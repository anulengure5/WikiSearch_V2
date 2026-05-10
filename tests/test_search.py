from utils.loader import load_docs
from core.indexer import build_index
from retrieval.search import search

def run_test():
    docs = load_docs()
    build_index(docs)

    results = search("machine learning")
    print("Results:", results)

if __name__ == "__main__":
    run_test()