#!/bin/bash

mkdir -p data/s3_openalex

aws s3 sync s3://openalex data/s3_openalex/
