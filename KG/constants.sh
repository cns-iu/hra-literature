# File with constants that the scripts/*.sh use

if [ -e db-config.sh ]; do
  source db-config.sh
done

DATA_DIR='./data'
REPORTS_DIR='./data/reports';
BASENAME=$DATA_DIR/hra-lit

GRAPH=https://purl.humanatlas.io/g/hra-lit/v0.1
SAFE_MODE=--unsafe
JNL=${BASENAME}.blazegraph.jnl
