# encoding: utf-8


class BaseModel(object):

    def serialize(self, allow_none=False):
        def serialize_func(obj):
            if isinstance(obj, BaseModel):
                ret = {}
                for k, v in vars(obj).items():
                    r = serialize_func(v)
                    if allow_none or r is not None:
                        ret[k] = r
                return ret
            elif isinstance(obj, list):
                return [serialize_func(o) for o in obj if allow_none or serialize_func(o) is not None]
            else:
                return obj.decode('utf-8') if isinstance(obj, bytes) else obj
        return serialize_func(self)

