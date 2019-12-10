# encoding: utf-8
class AXTExceptionCode:

    SUCCESS = 20000 # 成功
    PARAM_ERROR = 40000 # 参数错误
    FREQ_LIMIT = 40002  # 频繁调用
    UNAUTHORIZED = 40100    # 鉴权失败
    INACTIVE = 40301    # 未开通
    INSUFFICIENT_BALANCE = 40302    #余量不足
    NO_FACE = 40020 # 未检测到人脸
    ENTITY_TOO_LARGE = 41300 # 实体太大
    INTERNAL_ERROR = 50000  # 服务异常
    NOT_SUPPORT = 50101 # 不支持
    SYSTEM_BUSY = 50006 # 系统繁忙


class AXTExceptionMessage:

    SUCCESS = '成功'
    PARAM_ERROR = '参数错误'
    FREQ_LIMIT = '频繁调用'
    UNAUTHORIZED = '鉴权失败'
    INACTIVE = '未开通'
    INSUFFICIENT_BALANCE = '余量不足'
    NO_FACE = '未检测到人脸'
    ENTITY_TOO_LARGE = '实体太大'
    INTERNAL_ERROR = '服务异常'
    NOT_SUPPORT = '不支持'
    SYSTEM_BUSY = '系统繁忙'

class AXTBaseException(Exception):

    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message


class AXTEntityTooLargeException(Exception):

    def __init__(self):
        super().__init__(AXTExceptionMessage.ENTITY_TOO_LARGE)
        self.code = AXTExceptionCode.ENTITY_TOO_LARGE
        self.message = AXTExceptionMessage.ENTITY_TOO_LARGE


class AXTNotSupportException(Exception):

    def __init__(self):
        super().__init__(AXTExceptionMessage.NOT_SUPPORT)
        self.code = AXTExceptionCode.NOT_SUPPORT
        self.message = AXTExceptionMessage.NOT_SUPPORT
