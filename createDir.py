import os

def createDirectory(date):
    try:
        ## 만약 data 라는 경로가 없다면
        if not os.path.exists(date):
            ## 경로 생성
            os.makedirs(date)
    except OSError:
        print("Creation of the directory %s failed" % date)