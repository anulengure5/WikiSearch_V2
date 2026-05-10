import glob
import pickle
from collections import defaultdict

from storage.reader import read_postings_from_files
from storage.writer import write_index

def merge_indexes():

    posting_files = sorted(
        glob.glob("data/partial_postings_*.bin")
    )

    lexicon_files = sorted(
        glob.glob("data/partial_lexicon_*.pkl")
    )

    all_terms = set()

    for lexicon_path in lexicon_files:

        with open(lexicon_path, "rb") as f:
            lexicon = pickle.load(f)

            all_terms.update(lexicon.keys())

    merged_index = defaultdict(list)

    for term in sorted(all_terms):

        combined_postings = []

        for postings_path, lexicon_path in zip(
            posting_files,
            lexicon_files
        ):

            postings = read_postings_from_files(
                term,
                postings_path,
                lexicon_path
            )

            combined_postings.extend(postings)

        combined_postings.sort()

        merged_index[term] = combined_postings

    write_index(
        merged_index,
        "data/final_postings.bin",
        "data/final_lexicon.pkl"
    )

    print("Merge complete.")