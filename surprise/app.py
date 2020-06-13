from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsurprise                    # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/profilelist', methods=['GET'])
def read_profile():
    profiles = list(db.profiles.find({},{'_id':0}))
    return jsonify({'result': 'success'})

@app.route('/registration')
def registration_page():
    return render_template('registration.html')

@app.route('/registration', methods=['POST'])
def new_profile():
    # title_receive로 클라이언트가 준 title 가져오기
    print(request.form)
    name_receive = request.form['name_give']
    phonenumber_receive = request.form['phonenumber_give']
    birthday_receive = request.form['birthday_give']
    bank_receive = request.form['bank_give']
    account_receive = request.form['account_give']
    address_receive = request.form['address_give']
    password_receive = request.form['password_give']

    # DB에 삽입할 review 만들기
    profile = {
        'name': name_receive,
        'phonenumber': phonenumber_receive,
        'birthday': birthday_receive,
        'bank': bank_receive,
        'account': account_receive,
        'address': address_receive,
        'password': password_receive,
    }
    # reviews에 review 저장하기
    db.profiles.insert_one(profile)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '프로필이 등록되었습니다.'})
if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)