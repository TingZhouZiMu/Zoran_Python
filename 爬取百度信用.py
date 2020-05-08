import requests
import csv
import time

csvf = open('C:\\Users\\TingZhouZiMu\\Desktop\\Python\\baidu_companys.csv', 'a+', encoding='gbk', newline='')
writer = csv.writer(csvf)
writer.writerow(('company_name', 'legalPerson', 'regCap'))
url_temp = 'https://xin.baidu.com/s/l?q=%E8%85%BE%E8%AE%AF&t=0&p={page}&s=10&o=0&f=undefined'
for page in range(1, 11):
    time.sleep(1)
    url = url_temp.format(page=page)
    resp = requests.get(url)
    companys = resp.json()['data']['resultList']
    
    for company in companys:
        name = company['titleName']
        legalPerson = company['legalPerson']
        regCap = company['regCap']
        writer.writerow((name, legalPerson, regCap))
        print(page, name, legalPerson, regCap)
 
 
csvf.close()