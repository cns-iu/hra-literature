#!/bin/bash
set -e
source constants.sh

# Canonize all json files adding the JSON-LD context and outputting a combined nquads file
time cat data/*.json | ndjsonld canonize -c context.jsonld - data/hra-lit.nq --unsafe

# Load the nquads file into a blazegraph journal
time blazegraph-runner load --journal=data/hra-lit.blazegraph.jnl --use-ontology-graph=false --graph="https://purl.humanatlas.io/g/hra-lit/v0.1" --informat=turtle data/hra-lit.nq 

# Dump the turtle version of the graph from blazegraph
time blazegraph-runner dump --graph="https://purl.humanatlas.io/g/hra-lit/v0.1" --journal=data/hra-lit.blazegraph.jnl --outformat=turtle data/hra-lit.ttl
