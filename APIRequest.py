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
                                    headers=eval(headers)).json()
            else:
                res = requests.post(url=url,
                                    data=body,
                                    headers=headers).json()
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
                res = requests.get(url=url, params=eval(body)).json()
            else:
                res = requests.get(url=url, params=body).json()
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
    # lst=readExcel().getExcelcase("APItestcase.xlsx", "Sheet1")
    # for i in lst:
    #     result=APIRequest().GetRequests(i[0],i[1],i[2],i[3])
    #     print(result)
    r=APIRequest().GetRequests("http://bjga.chinamdm.com:12022//hermes/device/updateDeviceRootAndOut","post","{'Content-Type':'application/json'}","{'identifier':'14595bab68b4fd67663fdc6d4288d59d_1','recordNum':'1a啊/*-+~！@#￥%……&*（）——+·【】{}|、\?》《<>,.'}")
    print(json.loads(r))
