#!/usr/bin/env python

import jargparse

parser = jargparse.ArgParser('Convert Genbank GFF into an n-quad file')
parser.add_argument('gffPath', help='path to the GFF')
args = parser.parse_args()

accessionKey = '#!genome-build-accession NCBI_Assembly:'
accessionIdentifier = 'NONE FOUND'

with open(args.gffPath) as f:
    for line in f:
        if line.startswith(accessionKey):
            accessionIdentifier = line[len(accessionKey):]

print accessionIdentifier