#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

cd $DATA_DIR

for query in ${SRC}/sql/extract/*.sql; do
  echo `basename $query`
  time psql -f $query
done
