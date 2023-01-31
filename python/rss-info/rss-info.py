#!/usr/bin/env python
import feedparser
import sys
import json

url = ''

if len(sys.argv) > 1:
    url = sys.argv[1]
elif sys.stdin:
    url = str(sys.stdin.read())

ret = []

if url == '':
    exit(-1)

feed = feedparser.parse(url)

for post in feed.entries:
    ret.append({
        'title': post.title,
        'description': post.description
    })

print(json.dumps(ret))
