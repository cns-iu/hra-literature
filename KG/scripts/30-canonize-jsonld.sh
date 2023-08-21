#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

# Canonize all json files adding the JSON-LD context and outputting a combined nquads file
time cat $DATA_DIR/*.json | ndjsonld canonize -c context.jsonld - ${BASENAME}.nq $SAFE_MODE
