import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')
#print(titles)
#print(artists)
#print(ranking)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)

# movies (tr들) 의 반복문을 돌리기
for music in musics:
    #print(music)
    title=music.select_one('td.info > a.title.ellipsis')
    artist=music.select_one('td.info > a.artist.ellipsis')
    ranking=music.select_one('td.number')
    real_ranking=ranking.get_text()
    print(real_ranking[0:2].strip(),end=' ')
    print(title.get_text().strip(),end=' ')
    print(artist.get_text().strip())
    #print(artist.get_text().strip())
    #print(ranking)
    
     # movie 안에 a 가 있으면,
#     a_tag = title.select_one('td.title > div > a')
#     if title is not None:
#         rank = movie.select_one('td:nth-child(1) > img')['alt'] # img 태그의 alt 속성값을 가져오기
    #    title_text=soup.select_one(title).get_text()
#         title_text = $(title).text 
#        print('title_text')                                     # a 태그 사이의 텍스트를 가져오기
#         star = movie.select_one('td.point').text                # td 태그 사이의 텍스트를 가져오기
#         print(rank,title,star)