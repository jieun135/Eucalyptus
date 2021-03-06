import requests
from bs4 import BeautifulSoup

for page in range(1,52, 10): # for page in range(1,52, 10) [1, 11, 21,31,41,51]
    # page로 숫자로 지정할 수 있다.
    url = "https://search.naver.com/search.naver?where=news&query=%EC%86%90%ED%9D%A5%EB%AF%BC&start="+ str(page)
    row = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(row.text,'html.parser')

    # 컨테이너 : ul.type01>li
    # 제목 : a._sp_each_title
    # 신문사 : span._sp_each_source

    articles = html.select('ul.type01>li')
    for news in articles:
        title = news.select_one('a._sp_each_title')
        journal = news.select_one('span._sp_each_source').text.strip()
        print(title.text.strip() , journal)
    print("=================================================")