# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi
from ebaipy.exceptions import EbaiClientException


class EbaiMarketing(BaseEbaiApi):

    def present_coupon(self, **kwargs):
        """
        定向券发券接口

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_coupon_present

        :param user_id: 用户ID
        :param phone_no: 用户手机号码
        :param coupon_name: 优惠券名称，最多支持10个汉字
        :param baidu_shop_ids: 平台门店ID，支持多个，与第三方门店ID二选一，全部填写以平台门店ID为准 示例：2167002631;11112222
        :param shop_ids: 第三方门店ID，支持多个，与平台门店ID二选一，全部填写以平台门店ID为准 示例： 1432872160;2167002631
        :param threshold: 优惠券使用门槛，满X可用，正整数，单位分
        :param coupon_amount: 优惠券减免金额，满X减免Y，正整数，单位分
        :param is_conflict_activity: 是否与其他活动同享，0 同享，1 互斥 默认为同享
        :param begin_time: 优惠券生效时间，时间戳
        :param end_time: 优惠券失效时间，时间戳
        :return:
        """
        cmd = 'activity.coupon.present'

        body = kwargs

        return self._post(cmd, **{
            'body': body
        })

    def query_coupon(self,user_id, phone_no=None):
        """
        查看优惠券信息

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_coupon_query

        :param user_id: 用户ID
        :param phone_no: 用户手机号码

        :return:
        """
        cmd = 'activity.coupon.query'

        body = {
            'user_id': user_id
        }

        if phone_no:
            body['phone_no'] = phone_no

        return self._post(cmd, **{
            'body': body
        })

    def create(self, **kwargs):
        """
        创建商品营销活动

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_create

        :return:
        """
        cmd = 'activity.create'

        body = kwargs

        return self._post(cmd, **{
            'body': body
        })

    def disable(self, activity_id, baidu_shop_id=None, shop_id=None, supplier_id=None):
        """
        下线商品营销活动

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_disable

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店ID，与供应商ID、合作方门店ID三选一
        :param shop_id: 合作方门店ID，与供应商ID、平台门店ID三选一
        :param supplier_id: 供应商ID，与合作方门店ID、平台门店ID三选一

        :return:
        """
        cmd = 'activity.disable'

        body = {
            'activity_id': activity_id
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id
        elif supplier_id:
            body['supplier_id'] = supplier_id

        return self._post(cmd, **{
            'body': body
        })

    def get(self, activity_id, baidu_shop_id=None, shop_id=None, supplier_id=None):
        """
        查看活动信息

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_get

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店ID，与供应商ID、合作方门店ID三选一
        :param shop_id: 合作方门店ID，与供应商ID、平台门店ID三选一
        :param supplier_id: 供应商ID，与合作方门店ID、平台门店ID三选一

        :return:
        """
        cmd = 'activity.get'

        body = {
            'activity_id': activity_id
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id
        elif supplier_id:
            body['supplier_id'] = supplier_id

        return self._post(cmd, **{
            'body': body
        })

    def add_ns1_sku(self, activity_id, baidu_shop_id=None, shop_id=None, activity_skus=None, activity_custom_skus=None):
        """
        N选1添加活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_ns1_sku_add

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店ID，与合作方门店ID二选一
        :param shop_id: 合作方门店ID，与平台门店ID二选一
        :param activity_skus: 使用商品id的活动商品，与商品自定义id互斥。
            目前固定4个，结构 商品id:库存。
            sku_id_1:stock1;sku_id_2:stock2;sku_id_3:stock3;sku_id_4:stock4
        :param activity_custom_skus: 使用商品自定义id的活动商品，与商品id互斥。
            目前固定4个，结构 商品自定义id:库存。
            customer_sku_id_1:stock1;customer_sku_id_2:stock2;customer_sku_id_3:stock3;customer_sku_id_4:stock4;

        """
        cmd = 'activity.ns1.sku.add'

        body = {
            'activity_id': activity_id
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if activity_skus:
            body['activity_skus'] = activity_skus
        elif activity_custom_skus:
            body['activity_custom_skus'] = activity_custom_skus

        return self._post(cmd, **{
            'body': body
        })

    def batch_add_ns1_sku(self, sku_info=[]):
        """
        N选1批量添加活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_ns1_sku_add_batch

        :param sku_info: (数组)活动商品信息
        :return:
        """
        cmd = 'activity.ns1.sku.add.batch'

        if not sku_info:
            raise EbaiClientException(
                errno=10000,
                errmsg="活动商品信息为空"
            )

        body = {
            'skuInfo': sku_info
        }
        return self._post(cmd, **{
            'body': body
        })

    def delete_ns1_sku(self, activity_id, baidu_shop_id=None, shop_id=None):
        """
        N选1删除活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_ns1_sku_delete

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店ID，与合作方门店ID二选一
        :param shop_id: 合作方门店ID，与平台门店ID二选一
        :return:
        """
        cmd = 'activity.ns1.sku.delete'

        body = {
            'activity_id': activity_id
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def batch_delete_ns1_sku(self, activity_id, baidu_shop_id=None, shop_id=None, activity_skus=None,
                             activity_custom_skus=None):
        """
        N选1批量删除活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_add_batch

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店ID，与合作方门店ID二选一
        :param shop_id: 合作方门店ID，与平台门店ID二选一
        :param activity_skus: 使用商品id的活动商品，与商品自定义id互斥。
            一批最多100个。结构 直降->商品id:库存:优惠价格（单位分） 满减 ->商品id:库存。
            商品直降sku_id_1:stock:special_price;sku_id_2:stock:special_price...
            带sku维度限购格式：商品直降sku_id_1:stock:special_price:store_user_limit...
            eg: 直降 12345678:9999:123:1;23456789:8888:12:0 品类满减sku_id_1:stock;sku_id_1:stock;......
            eg: 满减 12345678:9999;23456789:8888
        :param activity_custom_skus: 使用商品自定义id的活动商品，与商品id互斥。一批最多100个。
            结构 直降->商品自定义id:库存:优惠价格（单位分） 满减 ->商品自定义id:库存。
            商品直降custom_sku_id:stock:special_price;...
            带sku维度限购格式：商品直降custom_sku_id_1:stock:special_price:store_user_limit...
            eg: 直降 12345678:9999:123:-1;23456789:8888:12:9999。品类满减custom_sku_id:stock;...
            eg: 直降 12345678:9999:123;23456789:8888:12

        :return:
        """
        cmd = 'activity.sku.add.batch'

        body = {
            'activity_id': activity_id
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if activity_skus:
            body['activity_skus'] = activity_skus
        elif activity_custom_skus:
            body['activity_custom_skus'] = activity_custom_skus

        return self._post(cmd, **{
            'body': body
        })

    def add_sku(self, activity_id, stock, baidu_shop_id=None, shop_id=None, sku_id=None, custom_sku_id=None, **kwargs):
        """
        添加活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_add

        :param activity_id: 活动id
        :param stock: 活动商品库存
        :param baidu_shop_id: 平台门店id，与合作方门店id互斥
        :param shop_id: 合作方门店id，与平台门店id互斥
        :param sku_id: 商品id，与商品自定义id互斥
        :param custom_sku_id: 商品自定义商品id，商品id互斥
        :param store_user_limit: `可选` “店/人”：活动时间内，单商品在每个店铺中，每个用户可以购买的数量上限。
            默认 0表示没有填(-1表示不限制)，范围1~9999。现在只支持直降活动，满减不要填。
        :param special_price: `可选` 商品活动价，单位分
        :return:
        """
        cmd = 'activity.sku.add'

        body = {
            'activity_id': activity_id,
            'stock': stock
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if sku_id:
            body['sku_id'] = sku_id
        elif custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def batch_add_sku(self, activity_id, baidu_shop_id=None, shop_id=None, activity_skus=None, activity_custom_skus=None):
        """
        批量添加活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_add_batch

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店id，与合作方门店id互斥
        :param shop_id: 合作方门店id，与平台门店id互斥
        :param activity_skus: 使用商品id的活动商品，与商品自定义id互斥。一批最多100个。
            结构 直降->商品id:库存:优惠价格（单位分） 满减 ->商品id:库存。
            商品直降sku_id_1:stock:special_price;sku_id_2:stock:special_price...
            带sku维度限购格式：商品直降sku_id_1:stock:special_price:store_user_limit...
            eg: 直降 12345678:9999:123:1;23456789:8888:12:0 品类满减sku_id_1:stock;sku_id_1:stock;......
            eg: 满减 12345678:9999;23456789:8888
        :param activity_custom_skus: 使用商品自定义id的活动商品，与商品id互斥。一批最多100个。
            结构 直降->商品自定义id:库存:优惠价格（单位分） 满减 ->商品自定义id:库存。
            商品直降custom_sku_id:stock:special_price;...
            带sku维度限购格式：商品直降custom_sku_id_1:stock:special_price:store_user_limit...
            eg: 直降 12345678:9999:123:-1;23456789:8888:12:9999。
            品类满减custom_sku_id:stock;...
            eg: 直降 12345678:9999:123;23456789:8888:12

        :return:
        """
        cmd = 'activity.sku.add.batch'

        body = {
            'activity_id': activity_id,
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if activity_skus:
            body['activity_skus'] = activity_skus
        elif activity_custom_skus:
            body['activity_custom_skus'] = activity_custom_skus

        return self._post(cmd, **{
            'body': body
        })

    def delete_sku(self, activity_id, baidu_shop_id=None, shop_id=None, sku_id=None, custom_sku_id=None):
        """
        删除活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_delete

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店id，与合作方门店id互斥
        :param shop_id: 合作方门店id，与平台门店id互斥
        :param sku_id: 商品id，与商品自定义id互斥
        :param custom_sku_id: 商品自定义商品id，商品id互斥
        :return:
        """
        cmd = 'activity.sku.delete'

        body = {
            'activity_id': activity_id,
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if sku_id:
            body['sku_id'] = sku_id
        elif custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        return self._post(cmd, **{
            'body': body
        })

    def batch_delete_sku(self, activity_id, baidu_shop_id=None, shop_id=None, sku_id=None, custom_sku_id=None):
        """
        批量删除活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_delete_batch

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店id，与合作方门店id互斥
        :param shop_id: 合作方门店id，与平台门店id互斥
        :param sku_id: 使用商品id的活动商品, 与商品自定义id互斥。
            用逗号分开的饿百商品id sku_id_1,sku_id_2...（一批最多100个）
            eg: 1234,2345,3456
        :param custom_sku_id: 使用商品自定义id的活动商品，与商品id互斥。
            用逗号分开的商品自定义ID custom_sku_id1,custom_sku_id2...（一批最多100个）
            eg: 1234,2345,3456

        :return:
        """
        cmd = 'activity.sku.delete.batch'

        body = {
            'activity_id': activity_id
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if sku_id:
            body['sku_id'] = sku_id
        elif custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        return self._post(cmd, **{
            'body': body
        })

    def sku_list(self, activity_id, baidu_shop_id=None, shop_id=None, supplier_id=None,
                 sku_id=None, custom_sku_id=None, page=1, page_size=20):
        """
        查看获得商品信息

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_list

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店ID，与供应商ID、合作方门店ID三选一
        :param shop_id: 合作方门店ID，与供应商ID、平台门店ID三选一
        :param supplier_id: 供应商ID，与合作方门店ID、平台门店ID三选一
        :param sku_id: 商品id，与商品自定义id互斥
        :param custom_sku_id: 商品自定义id，与商品id互斥
        :param page: 页码,默认为1
        :param page_size: 获取数量,1-100,默认20
        :return:
        """
        cmd = 'activity.sku.list'

        body = {
            'activity_id': activity_id,
            'page': max(page, 1),
            'page_size': min(page_size, 100)
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id
        elif supplier_id:
            body['supplier_id'] = supplier_id

        if sku_id:
            body['sku_id'] = sku_id
        elif custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        return self._post(cmd, **{
            'body': body
        })

    def update_sku(self, activity_id, baidu_shop_id=None, shop_id=None, sku_id=None, custom_sku_id=None, **kwargs):
        """
        更新活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_update

        :param activity_id: 活动id
        :param baidu_shop_id: 平台门店id，与合作方门店id互斥
        :param shop_id: 合作方门店id，与平台门店id互斥
        :param sku_id: 商品id，与商品自定义id互斥
        :param custom_sku_id: 商品自定义id，与商品id互斥
        :param stock: 活动商品库存
        :param store_user_limit: “店/人”：活动时间内，单商品在每个店铺中，每个用户可以购买的数量上限。
            默认 0表示没有填(-1表示不限制)，范围1~9999。现在只支持直降活动，满减不要填
        :param special_price: 商品活动价，单位分
        :return:
        """
        cmd = 'activity.sku.update'

        body = {
            'activity_id': activity_id,
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if sku_id:
            body['sku_id'] = sku_id
        elif custom_sku_id:
            body['custom_sku_id'] = custom_sku_id

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def batch_update_sku(self, activity_id, act_sku_info=[]):
        """
        批量更新活动商品

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_sku_update_batch

        :param activity_id: 活动id
        :param act_sku_info: (数组)活动商品信息
            baidu_shop_id: 平台门店id，与合作方门店id互斥
            shop_id: 合作方门店id，与平台门店id互斥
            sku_id: 商品id，与商品自定义id互斥
            custom_sku_id: 商品自定义id，与商品id互斥
            stock: 活动商品库存
            store_user_limit: “店/人”：活动时间内，单商品在每个店铺中，每个用户可以购买的数量上限。
                默认 0表示没有填(-1表示不限制)，范围1~9999。现在只支持直降活动，满减不要填
            special_price: 商品活动价，单位分
        :return:
        """
        cmd = 'activity.sku.update.batch'

        if not act_sku_info:
            raise EbaiClientException(
                errno=10000,
                errmsg="活动商品信息为空"
            )

        body = {
            'activity_id': activity_id,
            'act_sku_info': act_sku_info
        }

        return self._post(cmd, **{
            'body': body
        })

    def update(self, activity_id, **kwargs):
        """
        更新活动信息

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Marketing-activity_update

        :param activity_id: 活动id
        :param open_time: 活动开始时间段内，每天售卖开始时间，默认全天生效，24小时制。例如00:00 23:59
        :param close_time: 活动开始时间段内，每天售卖结束时间，默认全天生效，24小时制。例如00:00 23:59
        :param weekday: 活动开始时间段内，每周具体星期几支持，默认活动生效时间段内全周支持。0,1,2,3,4,5,6代表周日到周六
        :param day_limit: 每日限购X单，1-1000整数
        :param order_limit: 每单限购商品数量。直降用到，满减没用到。1-1000整数
        :param activity_desc: 活动的简介，前端用户看到的“优惠说明”，不超过30个字
        :param show_category: 店铺页活动商品的分类名称，不超过8个字
        :param promotion_sku_desc: 描述商品活动具体规则，出现在每个商品的列表页和详情页，不超过15个字
        :param baidu_shop_id: 平台门店ID，与供应商ID、合作方门店ID三选一
        :param shop_id: 合作方门店ID，与供应商ID、平台门店ID三选一
        :param supplier_id: 供应商ID，与合作方门店ID、平台门店ID三选一

        :return:
        """
        cmd = 'activity.update'

        body = {
            'activity_id': activity_id
        }

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })