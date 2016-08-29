'''
Created on 2016-7-31

@author: chinaYi
'''

import xlrd

from sse.ExcelException import ExcelException

class ReadXls:
    '''A class used to extract data from excel'''
    
    def __init__(self,filename):
        self.filename = filename
        self.sheet = xlrd.open_workbook(self.filename)
    
    def get_nsheets(self):
        return self.sheet.nsheets
    
    def get_sheetsName(self):
        return self.sheet.sheet_names()
           
    def getUserAndPassword(self, user_cols, passwd_cols, sheetNo = 0):
        sh = self.sheet.sheet_by_index(sheetNo)
        cols = sh.ncols;
        if cols > user_cols >= 0 and cols > passwd_cols >= 0:
            users = sh.col_values(user_cols)[1:]
            #[1:] for delete the labels
            passwords = [p[-6:] for p in sh.col_values(passwd_cols)[1:]]
            return zip(users,passwords)
        else:
            raise ExcelException('cols out of range')
            

if __name__ == '__main__':
    x = ReadXls('data.xls')
    print(x.get_nsheets())
    print(x.get_sheetsName())
    for u,p in x.getUserAndPassword(2, 7):
        print(u,p)
    