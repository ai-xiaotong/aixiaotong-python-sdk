# encoding: utf-8
from aixiaotong.common.base_model import BaseModel


class AXTCommonResponse(BaseModel):

    def __init__(self, code=None, message='', **kwargs):
        self.code = code
        self.message = message
