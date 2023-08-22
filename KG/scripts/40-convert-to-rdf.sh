#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

# Load the nquads file into a blazegraph journal
time blazegraph-runner load --journal=$JNL \
  --use-ontology-graph=false --graph="${GRAPH}" \
  --informat=turtle ${BASENAME}.nq 

# Dump the turtle version of the graph from blazegraph
time blazegraph-runner dump --journal=$JNL \
  --graph="${GRAPH}" \
  --outformat=turtle ${BASENAME}.ttl

# Download the CCF.OWL KG
CCF=https://purl.org/ccf/releases/2.2.1/ccf.owl
curl -L -o $DATA_DIR/ccf.owl $CCF
time blazegraph-runner load --journal=$JNL \
  --use-ontology-graph=false --graph=$CCF \
  --informat=rdfxml $DATA_DIR/ccf.owl

# Download hubmap rui_locations.jsonld
RUI=https://ccf-api.hubmapconsortium.org/v1/hubmap/rui_locations.jsonld
curl -L $RUI | jsonld canonize > $DATA_DIR/hubmap-rui_locations.nq
time blazegraph-runner load --journal=$JNL \
  --use-ontology-graph=false --graph=$RUI \
  --informat=turtle $DATA_DIR/hubmap-rui_locations.nq
