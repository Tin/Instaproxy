# -*- coding: utf-8 -*-
import os
import json
from django.db import models
from utils import fetch, dump
from datetime import datetime
from settings import DATA_ROOT


class TimelineVisitor(object):

    basedir = os.path.join(DATA_ROOT, 'timelines')

    def __init__(self, user_id):
        self.user_id = user_id
        self.min_id = None
        self.items = {}
    
    def get_user_feed_url(self):
        feed_url = 'http://instagr.am/api/v1/feed/user/%s/?' % self.user_id
        if self.min_id:
            feed_url += 'max_id=%s&' % self.min_id
        return feed_url
    
    def crawl(self):
        till_end = False
        while not till_end:
            previous_min_id = self.min_id
            self.visit()
            till_end = (self.min_id == previous_min_id)
    
    def pprint(self):
        pprint(self.items)
    
    def dump(self):
        filename = self.get_filename()
        dump(filename, json.dumps(self.items))
    
    def load_from_cache(self):
        filename = self.get_filename()
        with open(filename, 'r') as f:
            self.items = json.loads(f.read())

    def get_filename(self):
        return os.path.join(self.basedir, '%s-%s.%s' % (self.user_id, 'timeline', 'json'))

    def visit(self):
        url = self.get_user_feed_url()
        # print 'visit %s' % url
        js = fetch(url)
        d = json.loads(js)
        if d['status'] == 'ok':
            for item in d['items']:
                pk = int(item['pk'])
                if pk not in self.items:
                    self.items[pk] = item
        self.min_id = self.get_min_id()
        return d
    
    def get_timeline(self):
        if self.cached and not self.expired:
            if not len(self.items):
                self.load_from_cache()
        else:
            self.visit()
            self.dump()

        return self.items

    def get_min_id(self):
        if len(self.items):
            return min(self.items.keys())
        else:
            return None

    def clear_cache(self):
        if self.cached:
            filename = self.get_filename()
            return os.remove(filename)

    @property
    def cached(self):
        return os.path.exists(self.get_filename())

    @property
    def cached_time(self):
        return datetime.fromtimestamp(os.path.getmtime(self.get_filename()))

    @property
    def expired(self):
        now = datetime.now()
        delta = now - self.cached_time
        return delta.days > 0
