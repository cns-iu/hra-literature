#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

rm -f ${DATA_DIR}*.*
rm -f ${REPORTS_DIR}/*
