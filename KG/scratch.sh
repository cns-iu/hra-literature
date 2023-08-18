#!/bin/bash

#python3 build_graph.py
jsonld expand hra-lit.jsonld > hra-lit.expand.jsonld

echo "formatting"
# time rdf-formatter -o text/turtle \
#   --ns=hra-lit=https://purl.humanatlas.io/g/hra-lit/v0.1# \
#   --ns=schema=http://schema.org/ \
#   hra-lit.expand.jsonld - > hra-lit.js.ttl

time rdfpipe -o text/turtle \
  --ns=hra-lit=https://purl.humanatlas.io/g/hra-lit/v0.1# \
  --ns=schema=http://schema.org/ \
  hra-lit.expand.jsonld > hra-lit.py.ttl


jsonld expand hra-lit.jsonld | rdfpipe \
  -i application/ld+json -o text/turtle \
  --ns=hra-lit=https://purl.humanatlas.io/g/hra-lit/v0.1# \
  --ns=schema=http://schema.org/ \
  - > hra-lit.py.ttl

rdfpipe data/hra-lit.jsonld -o application/n-quads > data/hra-lit.nq
#jsonld canonize data/hra-lit.jsonld > data/hra-lit.nq

rapper -g --show-namespaces \
  -i nquads -o ntriples \
  --feature 'xmlns:hra-lit="https://purl.humanatlas.io/g/hra-lit/v0.1#"' \
  --feature 'xmlns:schema="http://schema.org/"' \
  data/hra-lit.nq > data/hra-lit.ttl

jq '.["@graph"]' ../hra-lit.jsonld | jq -c '.[]' > out.ndjson
./cli.js out.ndjson out.nq --context ../context.jsonld 
rapper out.nq -i nquads -o turtle > out.ttl
