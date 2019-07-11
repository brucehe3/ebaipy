# -*- coding: utf-8 -*-
import time
import random
import requests
import hashlib
import json
import inspect

from ebaipy.client.api.base import BaseEbaiApi


def _is_api_endpoint(obj):
    return isinstance(obj, BaseEbaiApi)


class BaseEbaiClient(object):

    API_BASE_URL = ''

    def __new__(cls, *args, **kwargs):
        self = super(BaseEbaiClient, cls).__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_api_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(self)
            setattr(self, name, api)
        return self

    def __init__(self, source, secret, verison='3'):
        self._http = requests.Session()
        self.source = source
        self.secret = secret
        self.version = verison
        self.encrypt = ''

    def _request(self, method, **kwargs):

        key = {
            'get': 'params',
            'post': 'data'
        }.get(method)

        cmd = kwargs.pop('cmd')
        body = kwargs.pop('body', {})

        body = self.request_body(cmd, body)

        kwargs[key] = body

        res = self._http.request(
            method=method,
            url=self.API_BASE_URL,
            **kwargs
        )
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            pass

        return self._handle_result(
            res, method, **kwargs
        )

    def _handle_result(self, res, method=None, **kwargs):
        return res

    def _md5(self, raw_data):

        md5 = hashlib.md5()
        md5.update(raw_data.encode('utf8'))

        return md5.hexdigest().upper()

    def get_ticket(self):
        """
        生成请求ticket
        :return:
        """
        raw_data = "{0}{1}".format(time.time() *10000, random.randint(100,999))
        ticket = self._md5(raw_data)

        return "%s-%s-%s-%s-%s" % (ticket[:8], ticket[8:12], ticket[12:16], ticket[16:20], ticket[20:])

    def request_body(self, cmd, body):

        data = {
            'cmd': cmd,
            'timestamp': int(time.time()),
            'ticket': self.get_ticket(),
            'version': self.version,
            'source': self.source,
            'encrypt': '',
            'body': json.dumps(body),
        }

        sign = self.get_sign(data)

        data['sign'] = sign

        return data

    def get_sign(self, data = {}):
        """
        签名
        :param data:
        :return:
        """

        data['secret'] = self.secret
        sign_data = []
        for k in sorted(data):
            sign_data.append("{0}={1}".format(k, data[k]))

        return self._md5('&'.join(sign_data))

    def get(self, **kwargs):
        return self._request(
            method='get',
            **kwargs
        )

    def post(self, **kwargs):
        return self._request(
            method='post',
            **kwargs
        )