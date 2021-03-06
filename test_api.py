import requests
import unittest
import json
import readExcel
import paramunittest
import parameterized
from APIRequest import APIRequest
import testdata.ExcelConfig as ExcelConfig

api_list = readExcel.readExcel().getExcelcase(ExcelConfig.ExcelName, ExcelConfig.ExcelSheet)
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
    def test_case01(self,url, method, headers, data, expect):
        r = APIRequest().GetRequests(url, method, headers, data)
        res = str(r)
        try:
            self.assertIn(str(expect), res) #判断期望是否在接口返回信息中
            resultdata.append("Pass")
        except AssertionError as e:
            resultdata.append(res)
            raise AssertionError
        finally:
            print(resultdata)


if __name__ == '__main__':
    unittest.main(verbosity=2)


