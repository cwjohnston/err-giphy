#!/usr/bin/env python

"""Interact with the Giphy API"""

import re
import json
import requests
import time
import logging
import urllib
import random
from datetime import datetime, timedelta

requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)

api_url = 'http://api.giphy.com/v1'

def search_gifs(api_key, query)
    endpoint = '/gifs/search'
    query_url = ""


t = "pizza cowboy"

encoded_t = urllib.quote_plus(t)
query_url = "http://api.giphy.com/v1/gifs/search?q=%s&api_key=%s" % (encoded_t,api_key)

response = requests.get(query_url)

try:
    gif_list = response.json()
except ValueError, e:
    print "error: %s" % e
    print "content: %s" % content

data = gif_list.get("data", None)

if data:
    count = len(data)
    if count == 0:
        print "No results"

random_index = random.randrange(count)
gif_dict = data[random_index]
images = gif_dict.get("images",None)
if images:
    original_image = images.get("original", None)
    if original_image:
        original_image_url = original_image.get("url",None)
    if original_image_url:
        print original_image_url
