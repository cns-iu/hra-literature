#!/usr/bin/env node

import { Command } from 'commander';
import { createReadStream, createWriteStream, readFileSync } from 'fs';
import ndjson from 'iterable-ndjson';
import jsonld from 'jsonld';

// Our CLI Program
const program = new Command();

program
  .name('ndjsonld')
  .argument('<ndjsonFile>')
  .argument('<outputQuads>')
  .option('-c, --context <contextFile>')
  .option('--unsafe')
  .action(async (inputFile, outputFile, { context, unsafe }) => {
    const source = inputFile === '-' ? process.stdin : createReadStream(inputFile, { autoClose: true });
    const output = outputFile === '-' ? process.stdout : createWriteStream(outputFile, { autoClose: true });
    const contextObject = JSON.parse(readFileSync(context))?.['@context'];

    for await (const obj of ndjson.parse(source)) {
      if (contextObject) {
        obj['@context'] = contextObject;
      }
      const nquads = await jsonld.canonize(obj, { safe: !unsafe, compactArrays: false });
      output.write(nquads);
    }
  });

program.parse(process.argv);
