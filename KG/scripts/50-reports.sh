#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

mkdir -p $REPORTS_DIR

for query in sparql/*.rq; do
  qname=$(basename ${query%.rq})
  echo $qname
  TSV=$REPORTS_DIR/${qname}.tsv
  CSV=$REPORTS_DIR/${qname}.csv
  blazegraph-runner select --journal=$JNL $query $TSV
  head -1 $TSV | perl -pe 's/\?//g' > $CSV
  tail -n +2 $TSV | csvformat -t -D ',' -U 0 | \
    perl -pe 's/\^\^\<http\:\/\/www\.w3\.org\/2001\/XMLSchema\#string\>//g' | \
    perl -pe 's/\^\^\<http\:\/\/www\.w3\.org\/2001\/XMLSchema\#integer\>//g' > $CSV
  #comunica-sparql $SPARQL_ENDPOINT -f $query -t text/csv > $REPORTS_DIR/${qname}.csv
done

rm -f $REPORTS_DIR/*.tsv