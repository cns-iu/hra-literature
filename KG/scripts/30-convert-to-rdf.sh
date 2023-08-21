#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

# Canonize all json files adding the JSON-LD context and outputting a combined nquads file
time cat data/*.json | ndjsonld canonize -c context.jsonld - $DATA_DIR/hra-lit.nq $SAFE_MODE

# Load the nquads file into a blazegraph journal
time blazegraph-runner load --journal=data/hra-lit.blazegraph.jnl \
  --use-ontology-graph=false --graph="${GRAPH}" \
  --informat=turtle $DATA_DIR/hra-lit.nq 

# Dump the turtle version of the graph from blazegraph
time blazegraph-runner dump --journal=$DATA_DIR/hra-lit.blazegraph.jnl \
  --graph="${GRAPH}" \
  --outformat=turtle $DATA_DIR/hra-lit.ttl
