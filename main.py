import crawler
import createDir as dir
from datetime import datetime

# 1. 사이트에서 내용 크롤링하기
crawler.getTitle()
crawler.getHref()
crawler.getDesc()

# 2. 이번달 디렉토리 없으면 생성
date = datetime.today()
month = date.strftime('%Y-%m')
# print(date)
dir.createDirectory(month)

# 3. 내용 저장
filename = date.strftime('test')
crawler.saveText(month, filename)