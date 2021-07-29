import requests
import unittest
import json
import readExcel
import paramunittest
import parameterized
from APIRequest import APIRequest

api_list = readExcel.readExcel().getExcelcase("APItestcase.xlsx", "Sheet1")
resultdata = []


# @paramunittest.parametrized(*api_list)
class TestAPIfunc(unittest.TestCase):
    # def setParameters(self, url, method, headers, data):
    #     self.url = str(url)
    #     self.method = str(method)
    #     self.headers = str(headers)
    #     self.data = str(data)

    def setUp(self):
        print("do something befor test.prepare environment")

    def tearDown(self):
        print("do something after test.Clean up")

    @parameterized.parameterized.expand(api_list)
    def test_case01(self,url, method, headers, data):
        # res=requests.post(url='http://192.168.1.21/justsy/rpc/msgPushByUser',data={'userNames':'yiying.zh','content':'hhhhh'},
        #                   headers={'Content-Type':'application/x-www-form-urlencoded'}).json()
        # r = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        # r = json.loads(r)
        r = APIRequest().GetRequests(url, method, headers, data)
        # r = APIRequest().GetRequests(self.url, self.method, self.headers, self.data)
        r = json.loads(r)
        resultdata.append(str(r))
        self.assertEqual(r["status"], 400)
        # print(resultdata)

if __name__ == '__main__':
    unittest.main(verbosity=2)


