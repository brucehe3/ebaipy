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

        kwargs = {}

        if shop_id:
            kwargs['shop_id'] = shop_id

        if baidu_shop_id:
            kwargs['baidu_shop_id'] = baidu_shop_id

        return self._post(cmd, **kwargs)