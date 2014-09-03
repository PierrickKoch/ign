#! /usr/bin/env python
"""Compact JSON

usage: %s in.json out.json
       or < in.json > out.json
       or < in.json | xclip -sel clip
"""
import sys
import json

if '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__ % sys.argv[0])
    sys.exit(0)

fp = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
data = json.load(fp)
fp.close()

fp = open(sys.argv[2], 'w') if len(sys.argv) > 2 else sys.stdout
json.dump(data, fp, separators=(',', ':'))
fp.close()
