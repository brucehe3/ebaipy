# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi
from ebaipy.exceptions import EbaiClientException


class EbaiSku(BaseEbaiApi):

    def brand_list(self, keyword, page=1):
        """
        获取品牌列表

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_brand_list

        :param keyword: 查询品牌关键字
        :param page: `可选`默认返回第一页的数据，每页显示100
        :return: 返回的 JSON 数据包
        """
        cmd = 'sku.brand.list'

        body = {'keyword': keyword, 'page': min(1, page)}

        return self._post(cmd, **{
            'body': body
        })

    def category_list(self, keyword='', depth=1, parent_id=0):
        """
        获取分类列表

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_category_list

        :param keyword: 查询分类关键字，为空时查询对应分类层级下全部分类信息
        :param depth: 分类层级,分为1、2、3级
        :param parent_id: 父分类id，1级分类的父类id为0，2级分类的父类id为1级分类id，3级分类的父类id为2级分类id
        :return: 返回的 JSON 数据包
        """
        cmd = 'sku.category.list'

        body = {
            'keyword': keyword,
            'depth': depth,
            'parent_id': parent_id,
        }

        return self._post(cmd, **{
            'body': body
        })

    def create(self, **kwargs):
        """
        商品上传

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_create

        :return:
        """
        cmd = 'sku.create'

        body = kwargs

        return self._post(cmd, **{
            'body': body
        })

    def delete(self, shop_id, **kwargs):
        """
        删除商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_delete

        :param shop_id: 合作方门店ID
        :param sku_id: `可选` 商品id，多个id以逗号连接，最多同时支持100个商品id,与custom_sku_id参数互斥
        :param custom_sku_id: `可选` 商品自定义ID,与sku_id参数互斥
        :return:
        """
        cmd = 'sku.delete'

        body = {
            'shop_id': shop_id
        }

        sku_id = kwargs.pop('sku_id', None)
        custom_sku_id = kwargs.pop('custom_sku_id', None)

        if not sku_id and not custom_sku_id:
            raise EbaiClientException(
                errno=10208,
                errmsg='缺少参数sku_id'
            )

        if sku_id and custom_sku_id:
            raise EbaiClientException(
                errno=1,
                errmsg='sku_id和custom_sku_id参数互斥'
            )

        if sku_id:
            body['sku_id'] = sku_id
        elif custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        return self._post(cmd, **{
            'body': body
        })

    def get_items_by_category_id(self, shop_id, category_id):
        """
        根据自定义分类获取商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_getItemsByCategoryId

        :param shop_id: 合作方门店ID
        :param category_id: 自定义分类ID（新增分类时返回的分类ID，用户端店铺详情页展示的分类）

        :return:
        """
        cmd = 'sku.getItemByCategoryId'

        body = {
            'shop_id': shop_id,
            'category_id': category_id
        }

        return self._post(cmd **{
            'body': body
        })

    def list(self, shop_id, **kwargs):
        """
        商品列表

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_list

        :param shop_id: 合作方门店ID

        :return:
        """
        cmd = 'sku.list'

        body = {'shop_id': shop_id}

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def _on_offline(self, cmd, shop_id, **kwargs):

        body = {'shop_id': shop_id}

        sku_id = kwargs.pop('sku_id', None)
        upc = kwargs.pop('upc', None)
        custom_sku_id = kwargs.pop('custom_sku_id', None)

        if not (sku_id and upc and custom_sku_id):
            raise EbaiClientException(
                errno=1,
                errmsg='缺少参数sku_id/upc/custom_sku_id 三选一'
            )

        if sku_id:
            body['sku_id'] = sku_id
        elif upc:
            body['upc'] = upc
        elif custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        return self._post(cmd, **{
            'body': body
        })

    def offline(self, shop_id, **kwargs):
        """
        商品下线

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_offline

        :param shop_id: 合作方门店ID
        :param sku_id: `可选`商品ID，多个id以逗号连接，最多同时支持100个商品id,与custom_sku_id upc互斥
        :param upc: `可选`商品upc编码，多个upc以逗号连接，最多同时支持100个upc，与sku_id custom_sku_id互斥
        :param custom_sku_id: `可选`商品自定义ID,与sku_id upc参数互斥,多个upc以逗号连接,最多同时支持100个
        :return:
        """
        cmd = 'sku.offline'

        return self._on_offline(cmd, shop_id, **kwargs)

    def offline_one(self, shop_id, **kwargs):
        """
        单个商品下线

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_offline_one

        :param shop_id: 合作方门店ID
        :param sku_id: `可选`商品ID，只支持单个，与custom_sku_id upc参数互斥
        :param upc: `可选`商品upc编码，只支持单个，与sku_id custom_sku_id参数互斥
        :param custom_sku_id: `可选`商品自定义ID，只支持单个，与sku_id upc参数互斥
        :return:
        """
        cmd = 'sku.offline.one'

        return self._on_offline(cmd, shop_id, **kwargs)

    def online(self, shop_id, **kwargs):
        """
        商品上线

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_online

        :param shop_id: 合作方门店ID
        :param sku_id: `可选`商品ID，多个id以逗号连接，最多同时支持100个商品id,与custom_sku_id upc互斥
        :param upc: `可选`商品upc编码，多个upc以逗号连接，最多同时支持100个upc，与sku_id custom_sku_id互斥
        :param custom_sku_id: `可选`商品自定义ID,与sku_id upc参数互斥,多个upc以逗号连接,最多同时支持100个
        :return:
        """
        cmd = 'sku.online'

        return self._on_offline(cmd, shop_id, **kwargs)

    def online_one(self):
        """
        单个商品上线

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_online_one

        :param shop_id: 合作方门店ID
        :param sku_id: `可选`商品ID，只支持单个，与custom_sku_id upc参数互斥
        :param upc: `可选`商品upc编码，只支持单个，与sku_id custom_sku_id参数互斥
        :param custom_sku_id: `可选`商品自定义ID，只支持单个，与sku_id upc参数互斥
        :return:
        """
        cmd = 'sku.online.one'

        return self._on_offline(cmd, shop_id, **kwargs)

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