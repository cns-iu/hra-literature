#!/bin/bash

IFS=$'\n' KEYWORDS=($(csvtool col 1 keywords.csv | tail -n +2))

for keyword in "${KEYWORDS[@]}"; do
    echo "Searching for keyword: $keyword"
    esearch -db pubmed -query "'$keyword'" | efetch -format medline > "output_${keyword}.txt"
done
