# AutoGitPush
매일매일 자동으로 git push 작업하기 위한 python 파일

## 동작
1. https://www.infoq.com/development/news/ 에서 1페이지의 내용을 크롤링 해온다
2. 크롤링 된 정보를 text 로 저장한다.
3. text 는 이번달 폴더에 오늘 날짜로 저장된다
4. cronTab 을 이용해 알아서 매일매일 해당 py 가 실행되도록 만든다
5. 끝!