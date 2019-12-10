# encoding: utf-8
import uuid

from aixiaotong.common.base_model import BaseModel


class AXTCommonRequest(BaseModel):

    def __init__(self):
        self.requestId = str(uuid.uuid1())

