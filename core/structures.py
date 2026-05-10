from collections import defaultdict

# Global shared structures (Phase 1 only)
index = defaultdict(list)   # term → [(docID, tf)]
df = defaultdict(int)       # term → document frequency
doc_len = {}                # docID → length
N = 0                       # total docs
avgdl = 0                   # average document length