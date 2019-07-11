# -*- coding: utf-8 -*-


class BaseEbaiApi(object):
    """
    Ebai api base class
    """

    def __init__(self, client=None):
        self._client = client

    def _get(self, cmd, **kwargs):
        kwargs['cmd'] = cmd
        return self._client.get(**kwargs)

    def _post(self, cmd, **kwargs):
        kwargs['cmd'] = cmd
        return self._client.post(**kwargs)