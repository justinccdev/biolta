#!/usr/bin/env python

import jargparse

parser = jargparse.ArgParser('Convert Genbank GFF into an n-quad file')
parser.add_argument('gffPath', help='path to the GFF')
args = parser.parse_args()

with open(args.gffPath):
    pass
