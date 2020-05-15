import requests
from bs4 import BeautifulSoup
import bs4
import csv
        
   
def getHTMLText(url):
    try:
        r=requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
def printUnivList(ulist,num):
    csvf = open(r'C:\Users\TingZhouZiMu\Desktop\Python\UniRank.csv', 'a+', encoding='gbk', newline='')
    writer = csv.writer(csvf)
    writer.writerow(('排名', '学校名称', '省市',"学校类型","总分"))
    tplt= "{0:^10}\t{1:{5}^10}\t{2:{5}^10}\t{3:{5}^10}\t{4:^10}"
    print(tplt.format("排名","学校名称","省市","学校类型","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],chr(12288)))
        writer.writerow((u[0],u[1],u[2],u[3],u[4]))
    csvf.close()

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,567) 

main()