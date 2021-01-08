import json

import requests


class BaseApi:
    # params={}

    # 获取token
    def get_token(self,corpid,corpsecret):
        data={
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params':{'corpid': corpid, 'corpsecret': corpsecret}
        }
        r=self.send(data)
        token = r.json()['access_token']
        return token

    def send(self,data:dict):
        # raw_data=json.dumps(data)
        # for key,value in self.params.items():
        #     raw_data=raw_data.replace("${"+key+"}",str(value))
        # data=json.loads(raw_data)
        # print(data)
        r=requests.request(**data)
        # print(json.dumps(r.json(),indent=2))
        return r
