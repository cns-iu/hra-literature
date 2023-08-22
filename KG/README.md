# KG Data Processor

Data processor to populate various data sources into a database and then extract to json to jsonld to RDF and into a SPARQL database for querying. A set of reports are generated from the created SPARQL database.

## Setup

You need access to the postgresql database and have created a db-config.sh (see [db-config.example.sh](./db-config.example.sh)). You will also need:

- `psql` PostgreSQL cli program
- Node.js 18+
- ndjsonld (`npm install -g ndjsonld`)
- [blazegraph-runner](https://github.com/balhoff/blazegraph-runner/)
- Docker with Docker Compose (only if locally hosting the sparql server)

## Running

To run the process from start to finish simply run `./run.sh`. All results then go into the data directory created in this directory.

## Local hosting of the sparql database

Run `docker compose up` from this directory after successfully completing the `./run.sh` command.
