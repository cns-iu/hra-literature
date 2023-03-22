#!/bin/bash
esearch -db pubmed -query "human atlas" | efetch -format medline > output.txt
