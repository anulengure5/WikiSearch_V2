import time
import os

from utils.loader import load_docs

from storage.partial_writer import process_chunks
from storage.merger import merge_indexes

from retrieval.search import search
from utils.wiki_parser import parse_wiki_dump


start = time.time()

docs = parse_wiki_dump(
    r"O:\FUTURE\WikiSearchEngineV2\simplewiki-latest-pages-articles.xml.bz2",
    limit_docs=50
)
process_chunks(docs, chunk_size=10)

mid = time.time()

merge_indexes()

end = time.time()


print("Chunk indexing time:", mid - start)
print("Merge time:", end - mid)
print("Total indexing time:", end - start)


postings_size = os.path.getsize(
    "data/final_postings.bin"
)

lexicon_size = os.path.getsize(
    "data/final_lexicon.pkl"
)

total_size = postings_size + lexicon_size

print("Final index size (MB):",
      total_size / (1024 * 1024))


queries = [
    "machine learning",
    "artificial intelligence",
    "neural networks",
    "computer science",
    "information retrieval"
]


query_times = []

for query in queries:

    q_start = time.time()

    results = search(query)

    q_end = time.time()

    query_times.append(q_end - q_start)

    print(query, "->", results[:3])


avg_query_time = (
    sum(query_times) / len(query_times)
)

print("Average query latency:",
      avg_query_time)