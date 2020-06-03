from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/list', methods=['POST'])
def write_list():
    name_receive= request.form['name_give']
    number_receive= request.form['number_give']
    address_receive= request.form['address_give']
    phonenumber_receive= request.form['phonenumber_give']
    order_list={
        name_receive= request.form['name_give']
        number_receive= request.form['number_give']
        address_receive= request.form['address_give']
        phonenumber_receive= request.form['phonenumber_give']
    }
    return jsonify({'result':'success', 'msg': '주문 등록'})


@app.route('/list', methods=['GET'])
def read_list():
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)