#'
import bibtexparser
import os

os.chdir("/Users/daknowles/Dropbox/daklab.github.io/publications/")

with open('publications.bib') as bibtex_file:
    bib_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)

for i in range(len(bib_database.entries)):
    bib_database.entries[i]["ID"] = bib_database.entries[i]["ID"].replace(".","_")
    if "abstract" in bib_database.entries[i]:
        bib_database.entries[i]["abstract"] = bib_database.entries[i]["abstract"].replace("  "," ").replace("\n"," ")
        if "Competing Interest Statement" in bib_database.entries[i]["abstract"]: 
            bib_database.entries[i]["abstract"] = bib_database.entries[i]["abstract"].split("Competing Interest Statement")[0]

with open('publications_clean.bib', 'w') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)

