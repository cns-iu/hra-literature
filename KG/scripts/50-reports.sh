#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

mkdir -p $REPORTS_DIR

for query in sparql/*.rq; do
  qname=$(basename ${query%.rq})
  echo $qname
  blazegraph-runner select --journal=$JNL $query $REPORTS_DIR/${qname}.tsv
done
