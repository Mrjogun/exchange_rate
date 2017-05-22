# exchange_rate

# 설명
 naver에서 환율정보(엔화)를 15초마다 크롤링하여 추가된 정보가 있다면 콘솔창에 출력해주는 프로그램이다.

# exe 실행파일로 생성하는 방법
 콘솔창에서 아래의 명령어를 입력하면, 단일 exe파일로 생성하여 사용할수 있다.
 (단, pyinstaller 모듈이 설치되어있어야 한다.)
  pyinstaller --onefile --icon="Cornmanthe3rd-Plex-Other-python.ico" "exchange-rate.py"
    --onefile :한개의 파일로 만듬. 초기로딩시 여러개의 파일일때보다 약간 느림.
    --icon=아이콘파일이름:  실행파일의 아이콘이름.