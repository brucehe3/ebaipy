# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi


class EbaiOrder(BaseEbaiApi):

    def agree_refund(self):
        """
        同意用户取消单/退单
        :return:
        """
        pass

    def call_delivery(self):
        """
        呼叫配送
        :return:
        """
        pass

    def cancel(self):
        """
        取消订单
        :return:
        """
        pass

    def cancel_delivery(self):
        """
        取消呼叫配送
        :return:
        """
        pass

    def cancel_list(self):
        """
        获取未处理取消单/退单
        :return:
        """
        pass

    def apply_claim(self):
        """
        批量发起订单索赔
        :return:
        """
        pass

    def get_claim(self):
        """
        批量查询订单索赔结果
        :return:
        """
        pass

    def query_claim(self):
        """
        批量查询订单索赔信息
        :return:
        """
        pass

    def complete(self):
        """
        订单送达
        :return:
        """
        pass

    def confirm(self):
        """
        确认订单
        :return:
        """
        pass

    def get_delivery(self):
        """
        获取订单配送信息
        :return:
        """
        pass

    def disagree_refund(self):
        """
        拒绝用户取消单/退单
        :return:
        """
        pass

    def create_express(self):
        """
        设置订单快递单号
        :return:
        """
        pass

    def get(self):
        """
        查看订单详情
        :return:
        """
        pass

    def get_delivery_fee_for_crowd(self):
        """
        获取众包订单配送费
        :return:
        """
        pass

    def convert_id(self):
        """
        订单号转换
        :return:
        """
        pass

    def taking_limited(self):
        """
        设置门店限单值
        :return:
        """
        pass

    def list(self):
        """
        查看订单列表
        :return:
        """
        pass

    def part_refund(self):
        """
        商户发起部分退款申请
        :return:
        """
        pass

    def get_part_refund(self):
        """
        查看部分退款订单详情
        :return:
        """
        pass

    def part_refund_untrelist(self):
        """
        获取未处理部分退单
        :return:
        """
        pass

    def complete_pick(self):
        """
        订单拣货完成
        :return:
        """
        pass

    def private_info(self):
        """
        获取订单隐私信息
        :return:
        """
        pass

    def get_remind(self):
        """
        获取商户未处理催单
        :return:
        """
        pass

    def reply_remind(self):
        """
        商户回复催单
        :return:
        """
        pass

    def sendout(self):
        """
        订单送出
        :return:
        """
        pass

    def get_status(self):
        """
        查看订单状态
        :return:
        """
        pass

    def stop_delivery(self):
        """
        配送异常不再配送
        :return:
        """
        pass

    def switch_self_delivery(self):
        """
        配送异常切自配送
        :return:
        """
        pass