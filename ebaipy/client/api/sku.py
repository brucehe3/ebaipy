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

    def online_one(self, shop_id, **kwargs):
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

    def batch_update_price(self, shop_id, **kwargs):
        """
        批量修改商品价格

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_price_update_batch

        :param shop_id: 合作方门店ID
        :param skuid_price: `可选` skuid对应销售价格与市场价格
            1.对应价格用于指定一批sku和每个sku的价格修改值；
            2.格式为"skuid:销售价格(必选),市场价格(可选);skuid:销售价格(必选),市场价格(可选)"，示例："6930463400823:10;6930463400823:100,110"；
            3.单位：分，范围：1~99999900；
            4.最多支持100个SKU同时修改
        :param upc_price: `可选` upc编码对应价格
            1.对应价格用于指定一批upc和每个upc的价格修改值；
            2.格式为"upc:销售价格(必选),市场价格(可选);upc:销售价格(必选),市场价格(可选)",示例："upc123:10;upc456:100,110"；
            3.单位：分，范围：1~99999900；
            4.最多支持100个UPC同时修改
        :param custom_sku_id: `可选` 商品自定义ID,与skuid_price upc_price参数互斥
            1.格式为"custom_sku_id:销售价格(必选),市场价格(可选);upc:销售价格(必选),市场价格(可选)",示例："upc123:10;upc456:100,110"；
            2.单位：分，范围：1~99999900；
            3.最多支持100个custom_sku_id同时修改
        :return:
        """
        cmd = 'sku.price.update.batch'

        body = {'shop_id': shop_id}

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def update_price(self, shop_id, **kwargs):
        """
        修改单个商品价格

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_price_update_one

        :param shop_id: 合作方门店ID
        :param skuid_price: `可选` skuid对应销售价格与市场价格
            1.对应价格用于指定该sku_id的价格修改值
            2.格式为"skuid:销售价格(必选),市场价格(可选)"，示例："15397158021:100,110", "15397158021:100"；
            3.单位：分，范围：1~99999900；
            4.只支持一个sku_id
        :param upc_price: `可选` upc编码对应销售价格与市场价格
            1.对应价格用于指定该upc的价格修改值；
            2.格式为"upc:销售价格(必选),市场价格(可选)"，示例："6930463400823:100,110", "6930463400823:100"；
            3.单位：分，范围：1~99999900；
            4.只支持一个upc
        :param custom_sku_id: `可选` custom_sku_id对应销售价格与市场价格
            1.对应价格用于指定该custom_sku_id的价格修改值；
            2.格式为"custom_sku_id:销售价格(必选),市场价格(可选)"，示例："123:100,110", "123:100"；
            3.单位：分，范围：1~99999900；
            4.只支持一个custom_sku_id
        :return:
        """
        cmd = 'sku.price.update.one'

        body = {'shop_id': shop_id}

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def create_shop_category(self, shop_id, parent_category_id, name, rank):
        """
        新增商户自定义分类

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_shop_category_create

        :param shop_id: 合作方门店ID
        :param parent_category_id: 父分类ID(新增分类时返回的分类ID,若该分类是一级分类时传0)
        :param name: 自定义分类名称(最大字符为50个字符)
        :param rank: 自定义分类排序优先级 ，最小值为1，最大值为100000，rank值较大的优先展示
        :return:
        """
        cmd = 'sku.shop.category.create'

        body = {
            'shop_id': shop_id,
            'parent_category_id': parent_category_id,
            'name':name,
            'rank': rank
        }

        return self._post(cmd, **{
            'body': body
        })

    def delete_shop_category(self, shop_id, category_id):
        """
        删除商户自定义分类

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_shop_category_delete

        :param shop_id: 合作方门店ID
        :param category_id: 自定义分类ID（新增分类时返回的分类ID，用户端店铺详情页展示的分类）
        :return:
        """
        cmd = 'sku.shop.category.delete'

        body = {
            'shop_id': shop_id,
            'category_id': category_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def get_shop_category(self, shop_id):
        """
        获取商户自定义分类

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_shop_category_get

        :param shop_id: 合作方门店ID
        :return:
        """
        cmd = 'sku.shop.category.get'

        body = {
            'shop_id': shop_id,
        }

        return self._post(cmd, **{
            'body': body
        })

    def map_shop_category(self, shop_id, **kwargs):
        """
        绑定商品与自定义分类

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_shop_category_map

        :param shop_id: 合作方门店ID
        :param sku_id: 商品ID(新增商品时返回的商品ID)
        :param custom_sku_id: 商品商家自定义ID, 与sku_id参数互斥
        :param category_id: 自定义分类ID（新增分类时返回的分类ID，用户端店铺详情页展示的分类），为空时表示删除商品与分类所有关系
        :param rank: 商品排序优先级 ，最小值为1，最大值为100000，rank值较大的优先展示
        :return:
        """
        cmd = 'sku.shop.category.map'

        body = {
            'shop_id': shop_id,
        }

        body.update(kwargs)
        return self._post(cmd, **{
            'body': body
        })

    def update_shop_category(self, shop_id, category_id, name, rank):
        """
        修改商家自定义分类

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_shop_category_update

        :param shop_id: 合作方门店ID
        :param category_id: 自定义分类ID（新增分类时返回的分类ID，用户端店铺详情页展示的分类
        :param name: 自定义分类名称(最大字符为50个字符)
        :param rank: 自定义分类排序优先级 ，最小值为1，最大值为100000，rank值较大的优先展示
        :return:
        """
        cmd = 'sku.shop.category.update'

        body = {
            'shop_id': shop_id,
            'category_id': category_id,
            'name': name,
            'rank': rank
        }

        return self._post(cmd, **{
            'body': body
        })

    def shop_customsku_list(self, shop_id, category_id, page=1, pagesize=20):
        """
        获取商户自定义分类下商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_shop_customsku_list

        :param shop_id: 合作方门店ID
        :param category_id: 自定义分类ID（新增分类时返回的分类ID，用户端店铺详情页展示的分类）
        :param page: 页码,默认为1
        :param pagesize: 该页商品数量,1-100,默认20
        :return:
        """
        cmd = 'sku.shop.customsku.list'

        body = {
            'shop_id': shop_id,
            'category_id': category_id,
            'page': page,
            'pagesize': pagesize
        }

        return self._post(cmd, **{
            'body': body
        })

    def map_shop_customsku(self, shop_id, sku_id, custom_sku_id=None):
        """
        绑定商品与自定义商品ID

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_shop_customsku_map

        :param shop_id: 合作方门店ID
        :param sku_id: 商品ID(新增商品时返回的商品ID)
        :param custom_sku_id: 第三方自定义商品ID(商户自定义),若传入此参数，则将绑定(或修改)sku_id与该id的关系，为空时，表示删除绑定关系
        :return:
        """
        cmd = 'sku.shop.customsku.map'

        body = {
            'shop_id': shop_id,
            'sku_id': sku_id,
        }

        if custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        return self._post(cmd, **{
            'body': body
        })

    def exist_stdupc(self, shop_id, upc):
        """
        跟进upc码查询是否平台标品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_stdupc_exist

        :param shop_id: 合作方门店ID
        :param upc: upc码
        :return:
        """
        cmd = 'sku.stdupc.exist'

        body = {
            'shop_id': shop_id,
            'upc': upc,
        }

        return self._post(cmd, **{
            'body': body
        })

    def batch_update_stock(self, shop_id, **kwargs):
        """
        批量修改商品库存

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_stock_update_batch

        :param shop_id: 合作方门店ID
        :param skuid_stocks: `可选` 	skuid对应库存数量。
            1.对应库存用于指定一批sku和每个sku的库存修改值；
            2.格式为"skuid:库存数;skuid:库存数"，示例："6930463400823:10;6930463400823:100"；
            3.库存范围：0~99999；
            4.最多支持100个SKU同时修改

        :param upc_stocks: `可选` upc编码对应库存数量。
            1.对应库存用于指定一批upc和每个upc的库存修改值；
            2.格式为"upc:库存数;upc:库存数"，示例："upc123:10;upc456:100"；
            3.库存范围：0~99999；
            4.最多支持100个UPC同时修改
        :param custom_sku_id: `可选` 商品自定义ID。
            1. 与skuid_stocks upc_stocks参数互斥;
            2.格式为"custom_sku_id:库存数;upc:库存数”,示例："upc123:10;upc456:100,110"；
            3.范围：1~99999900；
            4.最多支持100个custom_sku_id同时修改
        :return:
        """
        cmd = 'sku.stock.update.batch'

        body = {
            'shop_id': shop_id
        }

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def update_stock(self, shop_id, **kwargs):
        """
        修改单个商品库存

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_stock_update_one

        :param shop_id: 合作方门店ID
        :param skuid_stocks: `可选` sku_id对应库存数量。
            1.对应库存用于指定该sku_id库存修改值；
            2.格式为"sku_id:库存数"，示例："15397158021:10"；
            3.库存范围：0~99999；
            4.只支持一个sku_id
        :param upc_stocks: `可选` upc编码对应库存数量。
            1.对应库存用于指定该upc编码库存修改值；
            2.格式为"upc:库存数"，示例："6930463400823:10"；
            3.库存范围：0~99999；
            4.只支持一个upc
        :param custom_sku_id: `可选` custom_sku_id对应库存数量。
            1.对应库存用于指定该custom_sku_id库存修改值；
            2.格式为"custom_sku_id:库存数"，示例："123:10"；
            3.库存范围：0~99999；
            4.只支持一个custom_sku_id
        :return:
        """
        cmd = 'sku.stock.update.one'
        body = {
            'shop_id': shop_id
        }

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def update(self, shop_id, **kwargs):
        """
        商品修改

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_update

        :param shop_id: 合作方门店ID
        :param kwargs: 更多参数请参考 https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_update
        :return:
        """
        cmd = 'sku.update'
        body = {
            'shop_id': shop_id
        }

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def upload_rtf(self, shop_id, rtf_detail):
        """
        商品富文本详情上传

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Sku-sku_uploadrtf

        :param shop_id: 合作方门店ID
        :param rtf_detail: 富文本详情
        :return:
        """
        cmd = 'sku.uploadrtf'

        body = {
            'shop_id': shop_id,
            'rtf_detail': rtf_detail
        }

        return self._post(cmd, **{
            'body': body
        })