#!/bin/bash

KEYWORDS=$(csvtool col 1 keywords.csv | tail -n +2)

for keyword in $KEYWORDS; do
    esearch -db pubmed -query "'$keyword'" | efetch -format medline > "output_${keyword}.txt"
done
