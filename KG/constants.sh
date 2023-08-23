# File with constants that the scripts/*.sh use

if [ -e db-config.sh ]; then
  source db-config.sh
fi

SRC=`pwd`
DATA_DIR='./data'
REPORTS_DIR='./data/reports';
BASENAME=$DATA_DIR/hra-lit

GRAPH=https://purl.humanatlas.io/g/hra-lit/v0.1
#SAFE_MODE=--unsafe
SAFE_MODE=
JNL=${BASENAME}.blazegraph.jnl

# Official LOD server instance
#SPARQL_ENDPOINT=https://lod.humanatlas.io/sparql

# Local server via `docker compose up`
SPARQL_ENDPOINT=http://localhost:8080/blazegraph/namespace/kb/sparql
