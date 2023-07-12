#' Script to remove newlines and double spaces from abstracts
import bibtexparser
import os

os.chdir("/Users/daknowles/Dropbox/daklab.github.io/publications/")

with open('publications_raw.bib') as bibtex_file:
    bib_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)

for i in range(len(bib_database.entries)):
    bib_database.entries[i]["ID"] = bib_database.entries[i]["ID"].replace(".","_")
    if "month" in bib_database.entries[i]:
        del bib_database.entries[i]["month"]
    if "abstract" in bib_database.entries[i]:
        bib_database.entries[i]["abstract"] = bib_database.entries[i]["abstract"].replace("  "," ").replace("\n"," ")
        if "Competing Interest Statement" in bib_database.entries[i]["abstract"]: 
            bib_database.entries[i]["abstract"] = bib_database.entries[i]["abstract"].split("Competing Interest Statement")[0]

with open('publications.bib', 'w') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)

