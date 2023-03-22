chmod +x pubmedapi.sh
esearch -db pubmed -query "human atlas" | efetch -format medline > output.txt
