import requests
from bs4 import BeautifulSoup as bs4
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    
url = 'https://www.infoq.com/development/news/'
res = requests.get(url, headers=header)

soup = bs4(res.text, 'html.parser')
html1 = soup.select('.cards.no-style.boxes > li > .card__content > .card__data > .card__title > a')
html2 = soup.select('.cards.no-style.boxes > li > .card__content > .card__data > .card__excerpt')

title = [] # 제목 저장 
href = [] # 링크 저장 
desc = [] # 설명 저장

# 제목 리스트 return
def getTitle():
    for data in html1:
        data.text.replace('\n','')
        data.text.replace('\n\n','')
        title.append(data.text)

    return title

# 링크 리스트 return
def getHref():
    for data in html1:
        href.append(data.attrs['href'])

    return href

# 설명 리스트 return
def getDesc():
    for data in html2:
        desc.append(data.text)

    return desc

# 내용 저장
def saveText(month, filename):
    f = open("./"+month+"/"+filename+".text", "w")

    for i in range(len(title)):
        
        data = str(i+1)+" 번째 검색 내용 \n"+"제목 : "+title[i]+"\n"+"주소 : https://www.infoq.com/"+href[i]+"\n"+"설명 : "+desc[i]+"\n"

        f.write(data)

    f.close()