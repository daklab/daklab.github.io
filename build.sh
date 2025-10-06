#!/bin/bash

cat src/header.html > index.html

cat >>index.html <<EOL
<section id="highlighted">
<h4>Highlighted publications</h4>
EOL

cat publications/highlighted.html >> index.html

cat >>index.html <<EOL
</section>
<section id="working">
<h4>Under submission</h4>
EOL

cat publications/working.html >> index.html

cat >>index.html <<EOL
</section>
<section id="genetics">
<h4>Genetics</h4>
EOL

cat publications/genetics.html >> index.html

cat >>index.html <<EOL
</section>
<section id="ml">
<h4>Machine learning/statistics</h4>
EOL

cat publications/ml.html >> index.html

cat >>index.html <<EOL
</section>
<section id="ml">
<h4>Working</h4>
EOL

cat publications/old.html >> index.html

cat >>index.html <<EOL
</section>
EOL

cat src/footer.html >> index.html