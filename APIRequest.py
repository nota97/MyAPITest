import requests
import json
from readExcel import readExcel

class APIRequest():
    def send_post(self,url,headers,body):
        r=None
        #报错JSONDecodeError: Expecting property name enclosed in double quotes，即期望属性名用双引号括起来
        try:
            res = requests.post(url=url,
                                data=json.loads(body.replace("'", "\"")),
                                headers=json.loads(headers.replace("'", "\""))).json()
        except Exception as e:
            raise Exception("error：接口无法连接")
        else:
            r = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return r

    def send_get(self,url,body):
        return 0

    def GetRequests(self, url, method, headers, body):
        result=None
        if method == "post":
            result=self.send_post(url,headers,body)
        elif method == "get":
            result=self.send_get(url,body)
        else:
            print("method错误!!!")
        return result

if __name__ == '__main__':
    lst=readExcel().getExcelcase("testdata/APItestcase.xlsx", "Sheet1")
    for i in lst:
        result=APIRequest().GetRequests(i[0],i[1],i[2],i[3])
        print(result)

