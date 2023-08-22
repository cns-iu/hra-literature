#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

for query in sql/extract/*.sql; do
  psql -f $query
done
