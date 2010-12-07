# -*- coding: utf-8 -*-
from django.test import TestCase
from models import TimelineVisitor
from datetime import datetime


class TimelineVisitorTests(TestCase):

    def setUp(self):
        pass

    def test_there_should_have_no_max_id_in_the_begin(self):
        v = TimelineVisitor(311749)
        self.assertEquals('http://instagr.am/api/v1/feed/user/311749/?', v.get_user_feed_url())

    def test_visitor_should_know_max_id_after_each_visit(self):
        v = TimelineVisitor(311749)
        d = v.visit()
        self.assertTrue(v.min_id > 9999)

    def test_visitor_should_know_min_id_after_each_visit(self):
        v = TimelineVisitor(311749)
        d = v.visit()
        self.assertTrue(v.max_id > 9999)

    def test_should_use_min_id_as_max_id_in_next_query(self):
        v = TimelineVisitor(311749)
        v.visit()
        expected_visit_url = 'http://instagr.am/api/v1/feed/user/311749/?max_id=%s&' % v.min_id
        self.assertEquals(expected_visit_url, v.get_user_feed_url())

    def test_should_use_max_id_as_min_id_in_update_query(self):
        v = TimelineVisitor(311749)
        v.visit()
        expected_visit_url = 'http://instagr.am/api/v1/feed/user/311749/?min_id=%s&' % v.max_id
        self.assertEquals(expected_visit_url, v.get_user_feed_url(update=True))

    def test_min_id_should_change_after_each_step(self):
        v = TimelineVisitor(311749)
        v.visit()
        min_id_1 = v.min_id
        v.visit()
        min_id_2 = v.min_id
        self.assertNotEquals(min_id_1, min_id_2)

    def test_visitor_should_cache_feed_result(self):
        v = TimelineVisitor(311749)
        v.clear_cache()
        self.assertFalse(v.cached)
        v.get_timeline()
        self.assertTrue(v.cached)
    
    def test_visitor_should_able_to_limit_timeline_size(self):
        v = TimelineVisitor(311749)
        r = v.range(limit=5)
        self.assertEquals(5, len(r['pictures']))

    def test_visitor_should_tell_cache_time(self):
        v = TimelineVisitor(311749)
        v.get_timeline()
        today = datetime.now()
        self.assertEquals(datetime, type(v.cached_time))
        self.assertEquals(today.day, v.cached_time.day)
        self.assertEquals(today.month, v.cached_time.month)
        self.assertEquals(today.year, v.cached_time.year)

    def test_visitor_should_tell_if_cache_is_expired(self):
        v = TimelineVisitor(311749)
        self.assertEquals(False, v.expired)
