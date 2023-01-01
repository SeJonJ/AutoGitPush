import requests
from bs4 import BeautifulSoup as bs4
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

## 다른 사이트를 크롤링하기 위해서는 여기를 수정!!
## 단 다른 사이트는 파라미터를 요구할 수 있기 때문에 그 부분은 추가로 세팅해야함
url = 'https://www.infoq.com/development/news/'
res = requests.get(url, headers=header)

soup = bs4(res.text, 'html.parser')
## select 를 통해서 html 에 있는 각 요소들의 내용을 가져올 수 잇음
## 이때 . 은 html 에서 class 에 해당하며, # 은 html 에서 id 에 해당한다
html1 = soup.select('.cards.no-style.boxes > li > .card__content > .card__data > .card__title > a')
html2 = soup.select('.cards.no-style.boxes > li > .card__content > .card__data > .card__excerpt')

## 모든 내용은 list 로 저장
title = [] # 제목 저장 
href = [] # 링크 저장 
desc = [] # 설명 저장

# 제목 리스트 return
def getTitle():
    for data in html1:
        data.text.replace('\n','')
        data.text.replace('\n\n','')
        ## 파이썬에서 list 에 저장할때는 append 사용 => list.add 와 같은 의미
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
    ## w 는 쓰기 모드로 파일을 연다는 것을 의미
    f = open("./"+month+"/"+filename+".txt", "w")

    ## title 의 길이만큼, 즉 크롤링해온 내용만큼 for 문 시작
    for i in range(len(title)):
        
        ## 저장할 내용을 str 형태로 생성
        ## 반복문이니까 각 list 에서 i 번째 요소를 가져와서 str 로 저장한다
        data = str(i+1)+" 번째 검색 내용 \n"+"제목 : "+title[i]+"\n"+"주소 : https://www.infoq.com"+href[i]+"\n"+"설명 : "+desc[i]+"\n"

        ## 실제로 파일 f 에 내용을 쓰기 write
        f.write(data)

    f.close()