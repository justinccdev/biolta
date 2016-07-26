#!/usr/bin/env python

import jargparse

#################
### FUNCTIONS ###
#################
def parseMetadataForAccessionIdentifier(line):
    accessionKey = '#!genome-build-accession NCBI_Assembly:'

    if line.startswith(accessionKey):
        return line[len(accessionKey):]
    else:
        return None

"""
Return attributes of the record if it's a gene record.
Otherwise, return None.
"""
def parseRecord(record):
    components = record.split()
    type = components[2]
    rawConcatAttributes = components[8]

    attributes = {}

    if type == 'gene':
        rawAttributes = rawConcatAttributes.split(';')
        for a in rawAttributes:
            # print a
            (key, value) = a.split('=')
            attributes[key] = value

        return attributes
    else:
        return None

def writeNquads(outPath, accessionIdentifier, geneRecords):
    iriStub = "urn:"

    with open(outPath, 'w') as f:
        for id, geneRecord in geneRecords.iteritems():
            f.write('<%s%s> <%slocus> <%s%s> .\n' % (iriStub, accessionIdentifier, iriStub, iriStub, id))
            f.write('<%s%s> <%sname> "%s" .\n' % (iriStub, id, iriStub, geneRecord['Name']))

############
### MAIN ###
############
parser = jargparse.ArgParser('Convert Genbank GFF into an n-quad file')
parser.add_argument('gffPath', help='path to the GFF')
parser.add_argument('outPath', help='path to output the n-quads')
args = parser.parse_args()

metadataPrefix = '#'
idKey = 'locus_tag'

accessionIdentifier = 'NONE FOUND'
geneRecords = {}

with open(args.gffPath) as f:
    for line in f:
        line = line.strip()
        if line.startswith(metadataPrefix):
            res = parseMetadataForAccessionIdentifier(line)
            if res != None:
                accessionIdentifier = res
        else:
            attributes = parseRecord(line)
            if attributes != None:
                geneRecords[attributes[idKey]] = attributes

writeNquads(args.outPath, accessionIdentifier, geneRecords)
