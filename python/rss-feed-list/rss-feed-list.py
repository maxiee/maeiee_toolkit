#!/usr/bin/env python
"""
从 `MT_DATA/rss/feed_list.yaml` 下读取 Feed 列表，输出为 JSON 格式
"""
import os
import yaml
import json
from pathlib import Path

MT_DATA = os.environ.get('MT_DATA')

if not MT_DATA:
    exit(-1)

RSS_FEED_LIST_CONFIG = Path(MT_DATA).joinpath('rss')
RSS_FEED_LIST_CONFIG.mkdir(exist_ok=True)
RSS_FEED_LIST_CONFIG = RSS_FEED_LIST_CONFIG.joinpath('feed_list.yaml')

if not RSS_FEED_LIST_CONFIG.exists():
    exit(-1)

with open(RSS_FEED_LIST_CONFIG, 'r') as f:
    config = yaml.load(f, yaml.FullLoader)

    print(json.dumps(config))
