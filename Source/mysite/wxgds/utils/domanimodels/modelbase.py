# -*- coding: utf-8 -*-
import json

class ConvertToJson():
    #类信息序列化
    def convertToJson(self):
        return  json.dumps(self, default = lambda obj: obj.__dict__)