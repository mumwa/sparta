from flask import Flask, render_template, jsonify, request #플라스크에서 Flask, 탬플릿 파일 가져오기, 데이터를 json 형식으로 받아와주는 jsonify, 클라이언트->서버로 어떤 요청을 보낼지 정해주는 request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')#기본페이지에서
def home():#home으로 정의된 함수를 실행한다
    return render_template('index.html')#index.html을 찾아온다.


## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])#/reviews페이지에서..?Post요청을 받는다.
def write_review():#write_reivew라고 된 함수에서
    title_receive = request.form['title_give']#title_give가 있는지 살펴보겠다-(index.html Ajax에 있음) 그걸 title_receive에 넣는다.
    author_receive = request.form['author_give']#위와 같음
    review_receive = request.form['review_give']#위와 같음

    review = {
       'title': title_receive,
       'author': author_receive,
       'review': review_receive,
    }#받은 값들을 title: author:해서 키값으로 집어넣음

    db.reviews.insert_one(review)#dv review에 위에 dictionary를 넣는다
    
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})#


@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{'_id':0}))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)