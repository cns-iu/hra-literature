#!/bin/bash
#Output the compact diagram and detailed diagram in SVG format 

dot -Tsvg ./outputDir/diagrams/summary/relationships.real.compact.dot -o diagrams_compact.svg

dot -Tsvg ./outputDir/diagrams/summary/relationships.real.large.dot -o diagrams_large.svg