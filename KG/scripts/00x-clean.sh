#!/bin/bash
source constants.sh
shopt -s extglob
set -ev

rm -f *.*
rm -f ${REPORTS_DIR}/*
