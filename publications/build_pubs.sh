#!/bin/bash

#alias  jabref='java -jar /Applications/JabRef.app/Contents/java/app/JabRef-4.3.1.jar'
alias  jabref='/Applications/JabRef.app/Contents/MacOS/JabRef --debug'

# jabref -i publications.bib -m "((entrytype=inproceedings) and (keywords=mlstats))",ml_conf.html,website -n &
jabref -i publications.bib -m "keywords=mlstats",ml.html,website -n &
jabref -i publications.bib -m "keywords=genetics",genetics.html,website -n &
jabref -i publications.bib -m "keywords=working",working.html,website -n &
jabref -i publications.bib -m "keywords=dead",old.html,website -n &