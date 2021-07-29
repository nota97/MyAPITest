import unittest
import os
import common.HTMLTestRunner as HTMLTestRunner
import test_api
from readExcel import readExcel


path = os.path.split(os.path.realpath(__file__))[0]
report_path = os.path.join(path, 'result')
resultPath=os.path.join(report_path, "report.html")
# print(resultPath)


if __name__ == '__main__':

    suite = unittest.TestSuite()
    # suite = unittest.defaultTestLoader.discover('./', pattern='test_api.py')
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAPIfunc))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_api))
    # test=TestAPIfunc("test_case01")
    # suite.addTest(test)
    fp = open(resultPath, 'wb')   #打开result/20181108/report.html测试报告文件，如果不存在就创建
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')

    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    data = test_api.resultdata
    readExcel.addresultintoExcel("APItestcase.xlsx", "Sheet1", data)
