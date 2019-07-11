# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi


class EbaiSku(BaseEbaiApi):

    def brand_list(self):
        """
        获取品牌列表
        :return:
        """
        pass

    def category_list(self):
        """
        获取分类列表
        :return:
        """
        pass

    def create(self):
        """
        商品上传
        :return:
        """
        pass

    def delete(self):
        """
        删除商品
        :return:
        """
        pass

    def get_items_by_category_id(self):
        """
        根据自定义分类获取商品
        :return:
        """

    def list(self, shop_id, **kwargs):
        """
        商品列表
        :return:
        """
        cmd = 'sku.list'

        body = {'shop_id': shop_id}

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def offline(self):
        """
        商品下线
        :return:
        """
        pass

    def offline_one(self):
        """
        单个商品下线
        :return:
        """
        pass

    def online(self):
        """
        商品上线
        :return:
        """
        pass

    def online_one(self):
        """
        单个商品上线
        :return:
        """
        pass

    def batch_update_price(self):
        """
        批量修改商品价格
        :return:
        """
        pass

    def update_price(self):
        """
        修改单个商品价格
        :return:
        """
        pass

    def create_shop_category(self):
        """
        新增商户自定义分类
        :return:
        """
        pass

    def delete_shop_category(self):
        """
        删除商户自定义分类
        :return:
        """
        pass

    def get_shop_category(self):
        """
        获取商户自定义分类
        :return:
        """
        pass

    def map_shop_category(self):
        """
        绑定商品与自定义分类
        :return:
        """
        pass

    def update_shop_category(self):
        """
        修改商家自定义分类
        :return:
        """
        pass

    def shop_customsku_list(self):
        """
        获取商户自定义分类下商品
        :return:
        """
        pass

    def map_shop_customsku(self):
        """
        绑定商品与自定义商品ID
        :return:
        """
        pass

    def exist_stdupc(self):
        """
        跟进upc码查询是否平台标品
        :return:
        """
        pass

    def batch_update_stock(self):
        """
        批量修改商品库存
        :return:
        """
        pass

    def update_stock(self):
        """
        修改单个商品库存
        :return:
        """
        pass

    def update(self):
        """
        商品修改
        :return:
        """
        pass

    def upload_rtf(self):
        """
        商品富文本详情上传
        :return:
        """
        pass