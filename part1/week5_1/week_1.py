# 네이버 영화 데이터 수집

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn#",
                   headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dt.tit > a
    title = m.select_one("dt.tit > a").text
    # 평점 div.star_t1 a span.num
    score = m.select_one("div.star_t1 a span.num").text
    # 장르 dl.lst_dsc dl.info_txt1 dd a
    # 감독 dl.lst_dsc dl.info_txt1 dd a
    # 배우 dl.lst_dsc dl.info_txt1 dd a
    # select 함수 이용하는 방법
    info = m. select("dl.info_txt1 dd") # 개요, 감독, 배우에 대한 데이터가 리스트로 저장
    # 장르
    genre = info[0].select("a") # 또 하나의 리스트를 만들어 준 것
    # 감독
    director = info[1].select("a")
    # 배우
    actor = info[2].select("a")
    print(title)
    print(score)
    for g in genre:
        print(g.text)
    for d in director:
        print(d.text)
    for a in actor:
        print(a.text)

    print("*"*50)
