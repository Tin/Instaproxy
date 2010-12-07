# -*- coding: utf-8 -*-
import urllib2


def fetch(url):
    return urllib2.urlopen(url).read()

def dump(filename, content):
    with open(filename, 'w') as f:
        f.write(content)