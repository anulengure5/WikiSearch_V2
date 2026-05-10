import bz2
import xml.etree.ElementTree as ET


def parse_wiki_dump(path, limit_docs=None):

    docs = []

    doc_id = 0

    with bz2.open(path, "rb") as f:

        context = ET.iterparse(f, events=("end",))

        for event, elem in context:

            if elem.tag.endswith("page"):

                title = elem.findtext(
                    ".//{*}title",
                    default=""
                )

                text = elem.findtext(
                    ".//{*}text",
                    default=""
                )

                combined = f"{title} {text}"

                docs.append((doc_id, combined))

                doc_id += 1

                elem.clear()

                if (
                    limit_docs is not None
                    and doc_id >= limit_docs
                ):
                    break

    return docs


