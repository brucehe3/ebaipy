# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi
from ebaipy.exceptions import EbaiClientException


class EbaiCommon(BaseEbaiApi):

    def business_categories(self, category_id=None):
        """
        业态分类接口

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Common-common_businesscategories

        :param category_id: 分类ID
        :return:
        """
        cmd = 'common.businesscategories'

        body = {}
        if category_id:
            body['category_id'] = category_id

        return self._post(cmd, **{
            'body': body
        })

    def express_list(self):
        """
        快递公司列表
        :return:
        """
        cmd = 'common.expresslist'

        return self._post(cmd, **{
            'body': {}
        })

    def ip_list(self):
        """
        获取IP列表

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Common-common_iplist

        :return:
        """
        cmd = 'common.iplist'

        return self._post(cmd, **{
            'body': {}
        })

    def shop_categories(self, level=None, category_id=None):
        """
        商户分类信息接口

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Common-common_shopcategories

        :param level: 非必填；分类ID的级别；1或2
        :param category_id: 非必填；分类ID

        :return:
        """
        cmd = 'common.shopcategories'

        body = {}

        if level is not None:
            body['level'] = level

        if category_id is not None:
            body['category_id'] = category_id

        return self._post(cmd, **{
            'body': body
        })

    def shop_cities(self, pid=None):
        """
        城市信息接口文档

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Common-common_shopcities

        :param pid: `可选`城市ID
        :return:
        """
        cmd = 'common.shopcities'

        body = {}

        if pid is not None:
            body['pid'] = pid

        return self._post(cmd, **{
            'body': body
        })

    def upload_picture(self, url=None, data=None, return_type=None):
        """
        上传图片

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Common-picture_upload

        :param url: 合作方图片地址,和data属性二选一,都存在时以url为主
        :param data: 合作方图片的base64编码,和url二选一
        :param return_type: `可选` 为1时，返回url和water_url；非1时，只返回url
        :return:
        """
        cmd = 'picture.upload'

        body = {}
        if url:
            body['url'] = url
        elif data:
            body['data'] = data

        if return_type is not None:
            body['type'] = return_type

        return self._post(cmd, **{
            'body': body
        })