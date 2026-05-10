import pickle

from storage.compression import (
    vb_decode,
    delta_decode
)


def read_postings_from_files(
    term,
    postings_path,
    lexicon_path
):
    
    with open(lexicon_path, "rb") as f:
     lexicon = pickle.load(f)

    if term not in lexicon:
        return []

    offset = lexicon[term]

    with open(postings_path, "rb") as postings_file:

     postings_file.seek(offset)
   
#    meta data
     doc_count_encoded = postings_file.read(1)
     doc_count = vb_decode(doc_count_encoded)[0]
    
     doc_ids_len_encoded = postings_file.read(1)
     doc_ids_len = vb_decode(doc_ids_len_encoded)[0]

# compressed docIDs
     encoded_doc_ids = postings_file.read(doc_ids_len)
    
     delta_doc_ids = vb_decode(encoded_doc_ids)
     doc_ids = delta_decode(delta_doc_ids)
# read tf values

     encoded_tfs = postings_file.read(doc_count)
     tfs = vb_decode(encoded_tfs)

     postings = list(zip(doc_ids, tfs))
 
     return postings


