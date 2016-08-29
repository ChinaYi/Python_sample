'''
Created on 2016-8-9

@author: chinayi
'''

class ExcelException(Exception):
    '''A user defined exception extends Exception'''
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)
    

class HttpParameterException(Exception):
    '''A user defined exception extends Exception'''
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)