#!/usr/bin/env python

import jargparse

parser = jargparse.ArgParser('Convert Genbank GFF into an n-quad file')
parser.add_argument('gffPath', help='path to the GFF')
parser.add_argument('outPath', help='path to output the n-quads')
args = parser.parse_args()

metadataPrefix = '#'
accessionKey = '#!genome-build-accession NCBI_Assembly:'
locusTagAttributeKey = 'locus_tag='

accessionIdentifier = 'NONE FOUND'
locusTags = []

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
                attributes = rawAttributes.split(';')
                for a in attributes:
                    # print a
                    if a.startswith(locusTagAttributeKey):
                        locusTags.append(a[len(locusTagAttributeKey):])

with open(args.outPath, 'w') as f:
    for locusTag in locusTags:
        f.write('<%s> <locus> "%s" .\n' % (accessionIdentifier, locusTag))