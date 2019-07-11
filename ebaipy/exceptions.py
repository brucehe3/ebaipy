# -*- coding: utf-8 -*-
import six
from ebaipy.utils import to_binary, to_text


class EbaiException(Exception):

    def __init__(self, errno, errmsg):

        self.errno = errno
        self.errmsg = errmsg

    def __str__(self):
        _repr = 'Error code: {code}, message: {msg}'.format(
            code=self.errno,
            msg=self.errmsg
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)

    def __repr__(self):
        _repr = '{klass}({code}, {msg})'.format(
            klass=self.__class__.__name__,
            code=self.errno,
            msg=self.errmsg
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)


class EbaiClientException(EbaiException):
    """Ebai API client exception class"""

    def __init__(self, errno, errmsg, client=None,
                 request=None, response=None):
        super(EbaiClientException, self).__init__(errno, errmsg)
        self.client = client
        self.request = request
        self.response = response
