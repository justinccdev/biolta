#!/usr/bin/env python

import jargparse

parser = jargparse.ArgParser('Convert Genbank GFF into an n-quad file')
parser.add_argument('gffPath', help='path to the GFF')
args = parser.parse_args()

metadataPrefix = '#'
accessionKey = '#!genome-build-accession NCBI_Assembly:'
accessionIdentifier = 'NONE FOUND'

with open(args.gffPath) as f:
    for line in f:
        line = line.strip()
        if line.startswith(metadataPrefix):
            if line.startswith(accessionKey):
                accessionIdentifier = line[len(accessionKey):]
        else:
            components = line.split()
            type = components[2]
            rawAttributes = components[8]

            if type == 'gene':
                print rawAttributes

print 'accessionIdentifier [%s]' % accessionIdentifier