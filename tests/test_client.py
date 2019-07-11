# -*- coding: utf-8 -*-

import unittest
from ebaipy.client import EbaiClient


class EbaiClientTestCase(unittest.TestCase):

    source = '62950'
    secret = '2dd5b13be1b1de79'

    def setUp(self):
        self.client = EbaiClient(self.source, self.secret)

    def test_shop_get(self):

        res = self.client.shop.get(shop_id=1096)

        self.assertEqual(res['errno'], 0)

    def test_shop_list(self):

        res = self.client.shop.list()

        self.assertEqual(res['errno'], 0)

    def test_shop_create(self):

        pass