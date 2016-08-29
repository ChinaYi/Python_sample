'''
Created on 2016-8-11

@author: chinayi
'''

import xlwt

class WriteXls:
    '''
        A class used to write data to .xls
        Only support Excel Version 95 to 2003
    '''
    def __init__(self, filename):
        self.style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
            num_format_str='#,##0.00')
        self.style1 =xlwt.easyxf(num_format_str='D-MMM-YY')
        self.filename = filename
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('sheet1');
        
    def writeCell(self, r, c, data):
        '''
            r: The zero-relative number of the row in the worksheet to which the cell should be written.
            c: The zero-relative number of the col in the worksheet to which the cell should be written.
            data: The data value to be written.
        '''
        self.ws.write(r, c, data, style = self.style0)
    
    def save(self):
        self.wb.save(self.filename)
        
if __name__ == '__main__':
    wxls = WriteXls('example.xls');
    wxls.writeCell(0, 0, 'username')
    wxls.writeCell(0, 1, 'password')
    wxls.save()