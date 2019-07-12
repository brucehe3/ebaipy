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

    def test_sku_list(self):

        res = self.client.sku.list(1096, sku_id='1537513092827702')

        self.assertEqual(res['errno'], 0)

    def test_sku_brand_list(self):

        res = self.client.sku.brand_list('apple')

        self.assertEqual(res['errno'], 0)

    def test_sku_category_list(self):

        res = self.client.sku.category_list(depth=2, parent_id='151301831159451')

        self.assertEqual(res['errno'], 0)

    def test_sku_create(self):

        res = self.client.sku.create(
            shop_id=1096,
            upc='123456755444',
            name='香蕉300g',
            status=0,
            left_num=100,
            sale_price=1220,
            photos=[
                {
                    'is_master': 1,
                    'url': 'https://open-be.ele.me/1.jpg'
                }
            ]
        )
        self.assertEqual(res['errno'], 0)

    def test_sku_delete(self):

        res = self.client.sku.delete(1096)

        print(res)