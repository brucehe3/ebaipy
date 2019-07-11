# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.base import BaseEbaiClient
from ebaipy.client import api


class EbaiClient(BaseEbaiClient):

    """
    饿百 API 操作类
    """
    API_BASE_URL = 'https://api-be.ele.me/'

    shop = api.EbaiShop()
    sku = api.EbaiSku()
    order = api.EbaiOrder()
    marketing = api.EbaiMarketing()
    common = api.EbaiCommon()