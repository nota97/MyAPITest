import requests
import json
from readExcel import readExcel

class APIRequest():
    def send_post(self,url,headers,body):
        r=None
        #报错JSONDecodeError: Expecting property name enclosed in double quotes，即期望属性名用双引号括起来
        try:
            if (type(body) is not dict):
                res = requests.post(url=url,
                                    data=eval(body),
                                    headers=eval(headers),verify=False).json()
            else:
                res = requests.post(url=url,
                                    data=body,
                                    headers=headers,verify=False).json()
        except Exception as e:
            res = {'error': '接口无法连接'}
            raise Exception("error：接口无法连接")
        finally:
            r = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
            return r
        # return r

    def send_get(self,url,body):
        r = None
        try:
            if(type(body) is not dict):
                res = requests.get(url=url, params=eval(body),verify=False).json()
            else:
                res = requests.get(url=url, params=body,verify=False).json()
        except Exception as e:
            res = {'error': '接口无法连接'}
            raise Exception("error:接口无法连接")
        finally:
            r = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
            return r

    def GetRequests(self, url, method, headers, body):
        result=None
        if method == "post":
            result = self.send_post(url,headers,body)
        elif method == "get":
            result = self.send_get(url,body)
        else:
            print("method错误!!!")
        return result

if __name__ == '__main__':
    r=APIRequest().GetRequests("https://192.168.1.23:12313/neeting/push/data/18372023720",
                               "get",
                               "",
                               "{'neetingId':'1234567890'}")
    print(json.loads(r))
