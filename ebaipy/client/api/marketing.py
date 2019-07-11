# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi


class EbaiMarketing(BaseEbaiApi):

    def present_coupon(self):
        """
        定向券发券接口
        :return:
        """
        pass

    def query_coupon(self):
        """
        查看优惠券信息
        :return:
        """
        pass

    def create(self):
        """
        创建商品营销活动
        :return:
        """
        pass

    def disable(self):
        """
        下线商品营销活动
        :return:
        """
        pass

    def get(self):
        """
        查看活动信息
        :return:
        """
        pass

    def add_ns1_sku(self):
        """
        N选1添加活动商品
        """
        pass

    def batch_add_ns1_sku(self):
        """
        N选1批量添加活动商品
        :return:
        """
        pass

    def delete_ns1_sku(self):
        """
        N选1删除活动商品
        :return:
        """
        pass

    def batch_delete_ns1_sku(self):
        """
        N选1批量删除活动商品
        :return:
        """
        pass

    def add_sku(self):
        """
        添加活动商品
        :return:
        """
        pass

    def batch_add_sku(self):
        """
        批量添加活动商品
        :return:
        """
        pass

    def delete_sku(self):
        """
        删除活动商品
        :return:
        """
        pass

    def batch_delete_sku(self):
        """
        批量删除活动商品
        :return:
        """
        pass

    def sku_list(self):
        """
        查看获得商品信息
        :return:
        """
        pass

    def update_sku(self):
        """
        更新活动商品
        :return:
        """
        pass

    def batch_update_sku(self):
        """
        批量更新活动商品
        :return:
        """
        pass

    def update(self):
        """
        更新活动信息
        :return:
        """
        pass