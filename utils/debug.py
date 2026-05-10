from core.structures import index

def debug_query(query_terms):
    for term in query_terms:
        print(f"\nTerm: {term}")
        print("Postings:", index.get(term, []))