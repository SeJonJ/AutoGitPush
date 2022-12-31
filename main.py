import crawler
import createDir as dir
from datetime import datetime

# 데이터 가져오기
title = crawler.getTitle()
href = crawler.getHref()
desc = crawler.getDesc()

# 이번달 디렉토리 없으면 생성
date = datetime.today()
month = date.strftime('%Y-%m')
# print(date)
dir.createDirectory(month)

# 내용 저장
filename = date.strftime('%Y-%m-%d')
crawler.saveText(month, filename)