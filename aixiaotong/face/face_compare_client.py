# encoding: utf-8
import base64
import io
import json
import os

from aixiaotong.common.client import AXTCommonClient
from aixiaotong.common.common_request import AXTCommonRequest
from aixiaotong.common.common_response import AXTCommonResponse
from aixiaotong.exception import AXTBaseException, AXTExceptionCode, AXTEntityTooLargeException, AXTNotSupportException


class FaceCompareRequest(AXTCommonRequest):

    def __init__(self, imageA, imageB):
        super().__init__()
        self.imageA = imageA
        self.imageB = imageB


class FaceCompareResponse(AXTCommonResponse):

    def __init__(self, score=None, **kwargs):
        super().__init__(**kwargs)
        self.score = score


class FaceCompareClient(AXTCommonClient):
    url = 'https://api.ai-xiaotong.com/face/compare'
    IAMGE_MAX_BYTES = 5*1024*1024

    def __init__(self, ak_id, ak_secret):
        super().__init__(ak_id, ak_secret, FaceCompareClient.url)

    def compare(self, image_a, image_b):
        """

        :param image_a: file object|bytes|path，文件不能大于5M
        :param image_b: file object|bytes|path，文件不能大于5M
        :except AXTBaseException: 参考`AXTBaseException`
        :return: 相似度得分
        """
        image_a_bytes = FaceCompareClient._check_and_read_file(image_a)
        image_b_bytes = FaceCompareClient._check_and_read_file(image_b)
        body = FaceCompareRequest(base64.b64encode(image_a_bytes), base64.b64encode(image_b_bytes)).serialize()
        data_str = self.post(json.dumps(body, ensure_ascii=False))
        data = FaceCompareResponse(**json.loads(data_str))
        if data.code != AXTExceptionCode.SUCCESS:
            raise AXTBaseException(data.code, data.message)
        return data.score

    @staticmethod
    def _check_and_read_file(image):
        if isinstance(image, bytes):
            image_size = len(image)
            if image_size > FaceCompareClient.IAMGE_MAX_BYTES:
                raise AXTEntityTooLargeException()
            return image
        elif isinstance(image, io.IOBase):
            image.seek(0, io.SEEK_END)
            image_size = image.tell()
            image.seek(0, 0)
            if image_size > FaceCompareClient.IAMGE_MAX_BYTES:
                raise AXTEntityTooLargeException()
            return image.read()
        elif isinstance(image, str):
            image_size = os.path.getsize(image)
            if image_size > FaceCompareClient.IAMGE_MAX_BYTES:
                raise AXTEntityTooLargeException()
            with open(image, 'rb') as f:
                return f.read()
        else:
            raise AXTNotSupportException()
