# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi
from ebaipy.exceptions import EbaiClientException


class EbaiOrder(BaseEbaiApi):

    def agree_refund(self, order_id):
        """
        同意用户取消单/退单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_agreerefund

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.agreerefund'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def call_delivery(self, order_id):
        """
        呼叫配送

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_callDelivery

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.callDelivery'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def cancel(self, order_id, cancel_type, reason):
        """
        取消订单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_cancel

        :param order_id: 订单ID
        :param cancel_type: 取消原因分类，参见附录“取消原因分类”
        :param reason: 取消原因描述
        :return:
        """
        cmd = 'order.cancel'

        body = {
            'order_id': order_id,
            'type': cancel_type,
            'reason': reason
        }

        return self._post(cmd, **{
            'body': body
        })

    def cancel_delivery(self, order_id):
        """
        取消呼叫配送

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_cancelDelivery

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.cancelDelivery'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def cancel_list(self, baidu_shop_id=None, shop_id=None, page=1):
        """
        获取未处理取消单/退单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_cancellist

        :param baidu_shop_id: 平台门店ID
        :param shop_id: 合作方门店ID
        :param page: 查询页码,默认查询第一页

        :return:
        """
        cmd = 'order.cancellist'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {
            'page': page
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def apply_claim(self, claim_list=[]):
        """
        批量发起订单索赔

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_claim_apply

        :param claim_list: (数组)索赔订单信息列表
            order_id: 订单ID
            claim_reason: 索赔原因编码,使用通过order.claim.query获取的索赔原因编码,任选其一即可
            reason_detail: 填写的附加额外信息
        :return:
        """
        cmd = 'order.claim.apply'

        if not claim_list:
            raise EbaiClientException(
                errno=10000,
                errmsg="索赔订单信息列表为空"
            )
        body = {
            'claim_list': claim_list
        }
        return self._post(cmd, **{
            'body': body
        })

    def get_claim(self, order_ids=[]):
        """
        批量查询订单索赔结果

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_claim_get

        :param order_ids: 订单ID数组

        :return:
        """
        cmd = 'order.claim.get'

        if not order_ids:
            raise EbaiClientException(
                errno=10000,
                errmsg="订单号为空"
            )

        body = {
            'order_ids': order_ids
        }
        return self._post(cmd, **{
            'body': body
        })

    def query_claim(self, order_ids=[]):
        """
        批量查询订单索赔信息

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_claim_query

        :param order_ids: 订单ID数组

        :return:
        """
        cmd = 'order.claim.query'

        if not order_ids:
            raise EbaiClientException(
                errno=10000,
                errmsg="订单号为空"
            )

        body = {
            'order_ids': order_ids
        }

        return self._post(cmd, **{
            'body': body
        })

    def complete(self, order_id, phone=None):
        """
        订单送达

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_complete

        :param order_id: 订单ID
        :param phone: `可选`配送员电话，为空取商家联系电话

        :return:
        """
        cmd = 'order.complete'

        body = {
            'order_id': order_id
        }

        if phone:
            body['phone'] = phone

        return self._post(cmd, **{
            'body': body
        })

    def confirm(self, order_id):
        """
        确认订单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_confirm

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.confirm'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def get_delivery(self, order_id):
        """
        获取订单配送信息

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_delivery_get

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.delivery.get'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def disagree_refund(self, order_id, refuse_reason):
        """
        拒绝用户取消单/退单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_disagreerefund

        :param order_id: 订单ID
        :param refuse_reason: 拒绝原因,不超过100字

        :return:
        """
        cmd = 'order.disagreerefund'

        body = {
            'order_id': order_id,
            'refuse_reason': refuse_reason
        }

        return self._post(cmd, **{
            'body': body
        })

    def create_express(self, baidu_shop_id=None, shop_id=None, express_list=[]):
        """
        设置订单快递单号

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_express_create

        :param baidu_shop_id: 合作方门店ID
        :param shop_id: 平台门店ID
        :param express_list: 快递信息;数组
            order_id: 订单号
            express_id: 快递单号
            express_company: 快递名称

        :return:
        """
        cmd = 'order.express.create'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        if not express_list:
            raise EbaiClientException(
                errno=10000,
                errmsg="快递信息为空"
            )

        body = {
            'express_list': express_list
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def get(self, order_id):
        """
        查看订单详情

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_get

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.get'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def get_delivery_fee_for_crowd(self, order_id):
        """
        获取众包订单配送费

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-order_getDeliveryFeeForCrowd

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.getDeliveryFeeForCrowd'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def convert_id(self, order_id, eleme_order_id):
        """
        订单号转换

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_id_convert

        :param order_id: 订单ID
        :param eleme_order_id: 饿了么订单号;order.get接口中返回的eleme_order_id
        :return:
        """
        cmd = 'order.id.convert'

        body = {
            'order_id': order_id,
            'eleme_order_id': eleme_order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def taking_limited(self, baidu_shop_id=None, shop_id=None, limit_data=[]):
        """
        设置门店限单值

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_limited_taking

        :param baidu_shop_id: 合作方门店ID
        :param shop_id: 平台门店ID
        :param limit_data: 限单时间和数量
            startTime: 限单开始时间
            endTime: 限单结束时间
            order_limit_num: 该时间段内的限单数量

        :return:
        """
        cmd = 'order.limited.taking'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {
            'limit_data': limit_data,
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def list(self, **kwargs):
        """
        查看订单列表

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_list

        :param start_time: 起始时间戳
        :param end_time: 结束时间戳
        :param status: 订单状态
        :param page: 订单列表分页返回，该参数指定页数
        :param shop_id: 合作方门店ID
        :param baidu_shop_id: 平台门店ID
        :return:
        """
        cmd = 'order.list'

        body = kwargs

        return self._post(cmd, **{
            'body': body
        })

    def part_refund(self, order_id, products=[]):
        """
        商户发起部分退款申请

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_partrefund

        :param order_id: 订单ID
        :param products: 申请退款的商品信息
            sku_id: 商品的sku码,和upc,custom_sku_id三选一
            upc: 商品的upc编码,和sku_id,custom_sku_id三选一
            custom_sku_id: 商品的自定义编码ID,和sku_id,upc三选一
            number: 退款的该商品数量
        :return:
        """
        cmd = 'order.partrefund'

        if not products:
            raise EbaiClientException(
                errno=10000,
                errmsg="申请退款的商品信息为空"
            )

        body = {
            'order_id': order_id,
            'products': products
        }

        return self._post(cmd, **{
            'body': body
        })

    def get_part_refund(self, order_id):
        """
        查看部分退款订单详情

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_partrefund_get

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.partrefund.get'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def part_refund_untrelist(self, baidu_shop_id=None, shop_id=None, page=1):
        """
        获取未处理部分退单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_partrefund_untrelist

        :param baidu_shop_id: 合作方门店ID,可以和平台门店ID二选一
        :param shop_id: 平台门店ID,可以和合作方门店ID二选一
        :param page: 平台门店ID,可以和合作方门店ID二选一

        :return:
        """
        cmd = 'order.partrefund.untrelist'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {
            'page': page
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def complete_pick(self, order_id):
        """
        订单拣货完成

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_pickcomplete

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.pickcomplete'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def private_info(self, order_id):
        """
        获取订单隐私信息

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_privateinfo

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.privateinfo'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def get_remind(self, baidu_shop_id=None, shop_id=None, page=1, quantity=20):
        """
        获取商户未处理催单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_remind_get

        :param baidu_shop_id: 合作方门店ID 可以和平台门店ID二选一
        :param shop_id: 平台门店ID 可以和合作方门店ID二选一
        :param page: 当前页(默认第一页)
        :param quantity: 每页显示条数(默认20条)
        :return:
        """
        cmd = 'order.remind.get'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {
            'page': page,
            'quantity': quantity
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def reply_remind(self, order_id, reply_type, reply_msg=None):
        """
        商户回复催单

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_remind_reply

        :param order_id: 订单ID
        :param reply_type: 商家回复催单类型(1 备货中、2 已送出、3 天气原因、6 自定义)
        :param reply_msg: 商家回复催单文案(回复内容不超过30个汉字，回复类别选择自定义，此项必传)
        :return:
        """
        cmd = 'order.remind.reply'

        body = {
            'order_id': order_id,
            'reply_type': reply_type
        }

        if reply_type == 6:

            if not reply_msg:
                raise EbaiClientException(
                    errno=10000,
                    errmsg="reply_type为自定义时，reply_msg不能为空"
                )

            body['reply_msg'] = reply_msg

        return self._post(cmd, **{
            'body': body
        })

    def sendout(self, order_id, phone=None):
        """
        订单送出

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_sendout

        :param order_id: 订单ID
        :param phone: `可选`配送员电话，为空取商家联系电话

        :return:
        """
        cmd = 'order.sendout'

        body = {
            'order_id': order_id
        }

        if phone:
            body['phone'] = phone

        return self._post(cmd, **{
            'body': body
        })

    def get_status(self, order_id):
        """
        查看订单状态

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_status_get

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.status.get'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def stop_delivery(self, order_id):
        """
        配送异常不再配送

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_stopdelivery

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.stopdelivery'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })

    def switch_self_delivery(self, order_id):
        """
        配送异常切自配送

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Order_Up-order_switchselfdelivery

        :param order_id: 订单ID

        :return:
        """
        cmd = 'order.switchselfdelivery'

        body = {
            'order_id': order_id
        }

        return self._post(cmd, **{
            'body': body
        })