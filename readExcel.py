import os
import openpyxl

#读取项目路径
rootpath = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(rootpath, 'testdata')

class readExcel():
    def getExcelcase(self,filename,sheetname):
        cls=[]
        xpath=os.path.join(path,filename)
        file = openpyxl.load_workbook(xpath)
        sheet = file[sheetname]
        rows = sheet.max_row
        # sheet['A3']="http://192.168.1.21/justsy/rpc/msgPushByUser"
        # file.save('APItestcase.xlsx')
        for i in range(rows - 1):
            lst = []
            for j in range(sheet.max_column):
                lst.append(sheet.cell(i + 2, j + 1).value)
            cls.append(lst)
        #print(cls)
        return cls

    @classmethod
    def addresultintoExcel(self,filename,sheetname,data):
        xpath = os.path.join(path, filename)
        file = openpyxl.load_workbook(xpath)
        sheet = file[sheetname]
        rows = sheet.max_row
        col = sheet.max_column
        for i in range (rows-1):
            sheet.cell(i+2, col+1).value= data[i]
            print(sheet.cell(i+2, col+1).value)
        file.save(rootpath+"/result/"+filename)
        return 0

if __name__ == '__main__':
    a = ["pass","false"]
    readExcel().getExcelcase("APItestcase.xlsx", "Sheet1")
    readExcel().addresultintoExcel("APItestcase.xlsx", "Sheet1", a)


