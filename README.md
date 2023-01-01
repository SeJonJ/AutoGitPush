# AutoGitPush
매일매일 자동으로 git push 작업하기 위한 python 파일

## 동작 방법
1. https://www.infoq.com/development/news/ 에서 1페이지의 내용을 크롤링 해온다
2. 크롤링 된 정보를 text 로 저장한다.
3. text 는 이번달 폴더에 오늘 날짜로 저장된다
4. cronTab 을 이용해 알아서 매일매일 해당 py 가 실행되도록 만든다
5. 끝!

## gitPush.sh

```
#!/bin/bash

date=`date`
github_Id="github ID"
github_Token="github_Token 내용"
github_Address="github 주소"
sourceDir="소스 주소"
logFile="로그파일 주소 => ../push.log"

## 예시
## github_Id="SeJonJ"
## github_Token="git token"
## github_Address="github.com/SeJonJ/AutoGitPush.git"
## sourceDir="/home/sejon/gitrepo/AutoGitPush"
## logFile="../push.log"

cd $sourceDir

python3 main.py

echo "========= push Start (Date : $date) =========" && echo "========= push Start (Date : $date) =========" >>$logFile 2>&1

git add -A
echo "git add -A" >> $logFile>&1

git commit -m $date"news update"
echo "`git commit -m "$date news update"`" >> $logFile 2>&1

echo "git push!!" >> $logFile 2>&1
git push https://$github_Id:$github_Token@$github_Address >> $logFile 2>&1

echo "========= push OK (Date : $date) =========" && echo "========= push OK (Date : $date) =========" >> $logFile 2>&1
```

## cronTab
```
# git 쓰기 모드로 변경
chmod 750 gitPush.sh

# crontab 설정
crontab -e
00 18 * * * bash파일위치 => * 18 * * * /home/jsj/gitrepo/gitPush.sh
```