#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

# Canonize all json files adding the JSON-LD context and outputting a combined nquads file
time cat $DATA_DIR/*.json | ndjsonld canonize -c context.jsonld - ${BASENAME}.nq $SAFE_MODE

# Load the nquads file into a blazegraph journal
time blazegraph-runner load --journal=$JNL \
  --use-ontology-graph=false --graph="${GRAPH}" \
  --informat=turtle ${BASENAME}.nq 

# Dump the turtle version of the graph from blazegraph
time blazegraph-runner dump --journal=$JNL \
  --graph="${GRAPH}" \
  --outformat=turtle ${BASENAME}.ttl
