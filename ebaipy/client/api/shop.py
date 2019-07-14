# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ebaipy.client.api.base import BaseEbaiApi
from ebaipy.exceptions import EbaiClientException


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

    def create(self, **kwargs):
        """
        创建商户

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_create

        :return:
        """
        cmd = 'shop.create'

        body = kwargs

        return self._post(cmd, **{
            'body': body
        })

    def get_announcement(self, baidu_shop_id=None, shop_id=None):
        """
        获取商户公告

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_announcement_get

        :param baidu_shop_id: `可选`平台门店ID，与shop_id二选一
        :param shop_id: `可选`合作方门店ID，与平台门店ID二选一
        :return:
        """
        cmd = 'shop.announcement.get'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {}

        if baidu_shop_id is not None:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id is not None:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def set_announcement(self, baidu_shop_id=None, shop_id=None, content=None, descritption=None):
        """
        设置商户公告

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_announcement_set

        :param baidu_shop_id: `可选`平台门店ID，与shop_id二选一
        :param shop_id: `可选`合作方门店ID，与平台门店ID二选一
        :param content: 内容
        :param descritption: 简介，仅饿了么前端展示使用

        :return:
        """
        cmd = 'shop.announcement.set'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        if content is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="内容不能为空"
            )

        body = {
            'content': content
        }

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        if descritption:
            body['descritption'] = descritption

        return self._post(cmd, **{
            'body': body
        })

    def get_aptitude(self, baidu_shop_id=None, shop_id=None):
        """
        获取商户资质

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_aptitude_get

        :param baidu_shop_id: `可选`平台门店ID，与shop_id二选一
        :param shop_id: `可选`合作方门店ID，与平台门店ID二选一
        :return:
        """
        cmd = 'shop.aptitude.get'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {}
        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def get_apitude_types(self):
        """
        获取全部资质类型

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_announcement_gettypes

        :return:
        """
        cmd = 'shop.aptitude.gettypes'

        body = {}
        return self._post(cmd, **{
            'body': body
        })

    def upload_aptitude(self, **kwargs):
        """
        上传资质
        图片地址需先使用picture.upload接口转换，使用转化后地址传参

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_aptitude_upload

        :return:
        """
        cmd = 'shop.aptitude.upload'

        body = kwargs

        return self._post(cmd, **{
            'body': body
        })

    def get_busstatus(self, baidu_shop_id=None, shop_id=None, platform_flag=1):
        """
        查看商户的营业状态

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_busstatus_get

        :param baidu_shop_id: 合作方门店ID
        :param shop_id: 平台门店ID
        :param platform_flag: 来源平台,'1' 表示饿了么,'2' 表示饿了么星选

        :return:
        """
        cmd = 'shop.busstatus.get'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {
            'platformFlag': platform_flag,
        }
        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def close(self, baidu_shop_id=None, shop_id=None):
        """
        商户歇业

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_close

        :param baidu_shop_id: 合作方门店ID
        :param shop_id: 平台门店ID

        :return:
        """
        cmd = 'shop.close'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {}

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def batchupdate_id(self, baidu_shop_ids, shop_ids):
        """
        商户三方门店ID映射

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_id_batchupdate

        :param baidu_shop_ids: 平台门店ID(数组)
        :param shop_ids: 合作方门店ID(数组)

        :return:
        """
        cmd = 'shop.id.batchupdate'

        if not isinstance(baidu_shop_ids, list):
            raise EbaiClientException(
                errno=10000,
                errmsg="baidu_shop_ids 平台门店ID 应该是一个数组"
            )

        if not isinstance(shop_ids, list):
            raise EbaiClientException(
                errno=10000,
                errmsg="baidu_shop_ids 平台门店ID 应该是一个数组"
            )

        if len(baidu_shop_ids) != len(shop_ids):
            raise EbaiClientException(
                errno=10000,
                errmsg="baidu_shop_ids 和 shop_ids数组个数不匹配"
            )

        body = {
            'baidu_shop_ids': baidu_shop_ids,
            'shop_ids': shop_ids
        }

        return self._post(cmd, **{
            'body': body
        })

    def push_msg(self, shop_id, baidu_shop_id, msg_type, **kwargs):
        """
        门店状态变更消息通知

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_msg_push

        :param shop_id: 合作方门店ID
        :param baidu_shop_id: 平台门店ID
        :param msg_type: 消息类型。
            online：上线通知，取online_xxxx相关字段;
            offline：下线通知,取offline_xxxx相关字段；
            shop_open： 商户营业通知，取business_xx字段；
            shop_close：商户暂停营业通知,取business_xx字段；
            shop_pause:商户休息通知,取business_xx字段
        :return:
        """
        cmd = 'shop.msg.push'

        body = {
            'shop_id': shop_id,
            'baidu_shop_id': baidu_shop_id,
            'msg_type': msg_type,
        }

        body.update(kwargs)

        return self._post(cmd, **{
            'body': body
        })

    def offline(self, baidu_shop_id=None, shop_id=None):
        """
        下线商户

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_offline

        :param baidu_shop_id: 合作方门店ID
        :param shop_id: 平台门店ID

        :return:
        """
        cmd = 'shop.offline'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {}

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def open(self, baidu_shop_id=None, shop_id=None):
        """
        商户开业

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_open

        :param baidu_shop_id: 合作方门店ID
        :param shop_id: 平台门店ID

        :return:
        """
        cmd = 'shop.open'

        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {}

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def get_status(self, baidu_shop_id=None, shop_id=None):
        """
        查看商户状态

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_status_get

        :param baidu_shop_id: 合作方门店ID
        :param shop_id: 平台门店ID

        :return:
        """

        cmd = 'shop.status.get'
        if baidu_shop_id is None and shop_id is None:
            raise EbaiClientException(
                errno=10000,
                errmsg="平台门店ID，与shop_id二选一"
            )

        body = {}

        if baidu_shop_id:
            body['baidu_shop_id'] = baidu_shop_id
        elif shop_id:
            body['shop_id'] = shop_id

        return self._post(cmd, **{
            'body': body
        })

    def unbind_msg(self):
        """
        TODO 门店解绑消息推送(下行)
        :return:
        """
        pass

    def update(self, **kwargs):
        """
        修改商户

        详情请参考
        https://open-be.ele.me/dev/api/doc/v3/#api-Shop-shop_update

        :return:
        """
        cmd = 'shop.update'

        body = kwargs

        return self._post(cmd, **{
            'body': body
        })