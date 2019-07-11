# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi


class EbaiShop(BaseEbaiApi):

    def get(self, shop_id=None, baidu_shop_id=None):
        """
        查看商户

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_get

        :param shop_id: 合作方门店ID
        :param baidu_shop_id: 平台门店ID
        :return: 返回的 JSON 数据包
        """
        cmd = 'shop.get'

        body = {}

        if shop_id:
            body['shop_id'] = shop_id

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id

        return self._post(cmd, **{
            'body': body
        })

    def list(self, order_push=None, order_status_push=None, status=None, sys_status=None):
        """
        商户列表

        详情参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_list

        :param order_push: 商户订单推送状态;`该字段废弃使用` 允许值: 0, 1
        :param order_status_push: 商户订单状态推送状态;`该字段废弃使用` 允许值: 0, 1
        :param status: 商户营业状态;1:正常营业, 3:休息中 9:停止营业;`该字段废弃使用` 允许值: 1,3,9
        :param sys_status: 商户审核状态;1:新增商户,3:修改待审核商户, 4:审核未通过, 6:正常营业, 7:新增待审核商户 8:上线驳回 12:通过品控 允许值: 1, 3, 4, 6, 7, 8, 12
        :return: 返回的 JSON 数据包
        """
        cmd = 'shop.list'

        body = {}

        if order_push is not None:
            body['order_push'] = order_push

        if order_status_push is not None:
            body['order_status_push'] = order_status_push

        if status is not None:
            body['status'] = status

        if sys_status is not None:
            body['sys_status'] = sys_status

        return self._post(cmd, **{
            'body': body
        })

    def create(self):
        """
        创建商户
        :return:
        """
        pass