# encoding: utf-8
import hashlib
import time

import requests
from hashlib import sha1
import hmac
import base64


class AXTCommonClient(object):

    signature_format = '{method}\n{content_md5}\n{content_type}\n{date}'

    def __init__(self, ak_id, ak_secret, url):
        self.ak_id = ak_id
        self.ak_secret = ak_secret
        self.url = url

    @staticmethod
    def hmacSHA1(key, data):
        """

        :param key: SHA1 key, bytes
        :param data: data to signature, bytes
        :return bytes:
        """
        return hmac.new(key, data, sha1).digest()

    def post(self, body, content_type='application/json; charset=utf-8'):
        """

        :param body: post body string
        :param content_type:
        :return:
        """
        content_md5 = ''
        if body:
            content_md5_hash = hashlib.md5()
            content_md5_hash.update(body.encode('utf-8') if isinstance(body, str) else body)
            content_md5 = base64.b64encode(content_md5_hash.digest()).decode('utf-8')
        date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
        signature = base64.b64encode(AXTCommonClient.hmacSHA1(
            self.ak_secret.encode('utf-8'),
            AXTCommonClient.signature_format.format(
                method='POST', content_md5=content_md5, content_type=content_type,
                date=date).encode('utf-8')
        )).decode('utf-8')
        authorization = 'AXT-HMAC-SHA1 {}:{}'.format(self.ak_id, signature)
        resp = requests.post(self.url, data=body, headers={
            'authorization': authorization,
            'content-md5': content_md5,
            'content-type': content_type,
            'date': date,
            'content-length': str(len(body))
        })
        return resp.content.decode('utf-8')
