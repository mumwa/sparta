# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbsparta 

# ## 코딩 할 준비 ##

# # mattrix = db.movies.find_one({'title':'매트릭스'},{'star':True})
# # print(mattrix)

# found_movie=db.movies.find_one({'title':'매트릭스'})
# print(found_movie['star'])

# # 그 중 특정 키 값을 빼고 보기
# # user = db.users.find_one({'name':'bobby'},{'_id':False})
# # print(user)

# same_stars = list(db.movies.find({'star':found_movie['star']},{'title':True}))
# print(same_stars)

#데이터 베이스에서 찾는게 빠름. 파이썬으로 가져와서 찾으면 오래 걸려~

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])
    db.movies.update_one({'title':movie['title']},{'$set':{'star':0}})