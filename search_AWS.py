#!/usr/bin/env python3


import requests

base = "https://nemo-public-preview.s3.us-east-1.amazonaws.com/other/grant/u01_lein/lein/transcriptome/"

candidates = [
    "README.txt",
    "metadata.csv",
    "manifest.json"
]

for c in candidates:
    url = base + c
    r = requests.head(url)
    print(url, r.status_code)
