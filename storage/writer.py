import pickle

# from core.structures import index



from storage.compression import (
    delta_encode,
    vb_encode
)

def write_index(index,
        postings_path="data/postings.bin",
        lexicon_path="data/lexicon.pkl"
):
    lexicon={
    }

    with open(postings_path,"wb") as f:
       
       for term in sorted(index.keys()):
          offset=f.tell()
          lexicon[term]=offset

          postings=index[term]

          doc_ids=[docID for docID,tf in postings]
          tfs=[tf for docID, tf in postings]

          delta_doc_ids=delta_encode(doc_ids)

          encoded_doc_ids=vb_encode(delta_doc_ids)
          encoded_tfs=vb_encode(tfs)

          doc_count=len(doc_ids)

          encoded_doc_count=vb_encode([doc_count])
          encoded_doc_ids_len=vb_encode([len(encoded_doc_ids)])

          f.write(encoded_doc_count)
          f.write(encoded_doc_ids_len)
          f.write(encoded_doc_ids)
          f.write(encoded_tfs)

    with open(lexicon_path,"wb") as lf:
             pickle.dump(lexicon,lf)

    print("Index written to disk.")
