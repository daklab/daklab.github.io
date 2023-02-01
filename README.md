# daklab.github.io

* [Google Scholar profile](https://scholar.google.com/citations?user=N9QGV6YAAAAJ)
* [LeafCutter](https://davidaknowles.github.io/leafcutter/) RNA splicing analysis
* [EAGLE](https://github.com/davidaknowles/eagle) software for detecting GxE interactions from RNA-seq using allele specific expression
* On twitter at [@david_a_knowles](https://twitter.com/david_a_knowles)

# Notes on updating

* To upload publications add them to publications/publications.bib, with one of the keywords used in publications/build_pubs.sh (currently mlstats,genetics or working). Then run the jabref commands in publications/build_pubs.sh. 
* To update photos, add to photos/ and then to the code at the end of src/footer.html. 
* Finally run ./build.sh to make a new index.html. 

# Banner credit

Photo by <https://unsplash.com/@davidhiggins>

# Compile (Mac OS X)

Through the GUI set jabref preference to sort by original order. Create a new "export format" called "website" using "publications/jabref_list_layout/listrefs.layout". 

Then on the command line:
```
alias jabref='java -jar /Applications/JabRef.app/Contents/java/app/JabRef-4.0-beta3.jar'
/publications/build_pubs.sh
./build.sh
```

# Original html5up README

Read Only by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)

Just a super simple single-page responsive template built for personal sites and portfolios
(although it'd definitely work for other stuff too). Includes a contact form, pre-styled
elements, and Sass sources.

Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.

(* = Not included)

Feedback, bug reports, and comments are not only welcome, but strongly encouraged :)

AJ
aj@lkn.io | @ajlkn

PS: Not sure how to get that contact form working? Give formspree.io a try (it's awesome).

Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fortawesome.github.com/Font-Awesome)

	Other:
		jQuery (jquery.com)
		html5shiv.js (@afarkas @jdalton @jon_neal @rem)
		CSS3 Pie (css3pie.com)
		Respond.js (j.mp/respondjs)
		Skel (skel.io)
