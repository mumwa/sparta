import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')
for music in musics:
    title=music.select_one('td.info > a.title.ellipsis')
    artist=music.select_one('td.info > a.artist.ellipsis')
    ranking=music.select_one('td.number')
    real_ranking=ranking.get_text()
    print(real_ranking[0:2].strip(),end=' ')
    print(title.get_text().strip(),end=' ')
    print(artist.get_text().strip())