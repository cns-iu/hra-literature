#!/bin/bash
#Output the compact diagram and detailed diagram in SVG format 

dot -Tsvg data/db/outputDir/diagrams/summary/relationships.real.compact.dot -o data/db/diagrams_compact.svg

dot -Tsvg data/db/outputDir/diagrams/summary/relationships.real.large.dot -o data/db/diagrams_large.svg