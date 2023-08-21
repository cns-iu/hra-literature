#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

rm -f ${BASENAME}.*
rm -f ${REPORTS_DIR}/*
