from __future__ import absolute_import, unicode_literals

from ebaipy.client import EbaiClient

__version__ = '0.1'
__author__ = 'Bruce He'


if __name__ == '__main__':

    client = EbaiClient('62950', '2dd5b13be1b1de79')

    res = client.shop.get()

    print(res.json())