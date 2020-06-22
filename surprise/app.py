from flask import Flask, render_template, jsonify, request
from bson.objectid import ObjectId
app = Flask(__name__)

from pymongo import MongoClient           
# client = MongoClient('localhost',27017) 
client = MongoClient('localhost',27017) 
db = client.dbsurprise                   

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/profilelist', methods=['GET'])
def read_profile():
    profiles = list(db.profiles.find({}))
    for profile in profiles:
        profile['_id'] = profile['_id'].__str__()
    
    # print(profiles[0])
    # ObjectId(string_id_from_front)
    # print(db.profiles.find_one({"_id": ObjectId(profiles[0]['_id'])}))
    # 아이디 가져다쓰는...그런거...
    return jsonify({'result': 'success', 'profiles': profiles})

@app.route('/registration')
def registration_page():
    return render_template('registration.html')

@app.route('/registration', methods=['POST'])
def new_profile():
    
    print(request.form)
    name_receive = request.form['name_give']
    phonenumber_receive = request.form['phonenumber_give']
    birthday_receive = request.form['birthday_give']
    bank_receive = request.form['bank_give']
    account_receive = request.form['account_give']
    address_receive = request.form['address_give']
    password_receive = request.form['password_give']

    
    profile = {
        'name': name_receive,
        'phonenumber': phonenumber_receive,
        'birthday': birthday_receive,
        'bank': bank_receive,
        'account': account_receive,
        'address': address_receive,
        'password': password_receive,
    }
    
    db.profiles.insert_one(profile)
    
    return jsonify({'result': 'success', 'msg': '프로필이 등록되었습니다.'})

@app.route('/giftsubmit')
def gift_submit_page():
    return render_template('gift_submit.html')

@app.route('/giftsubmit', methods=['POST'])
def new_gift():
    print(request.form)
    product_name_receive = request.form['product_name_give']
    price_receive = request.form['price_give']
    image_receive = request.form['image_give']
    link_receive = request.form['link_give']
    story_receive = request.form['story_give']
    user_id_receive = request.form['user_id']
    
    gift = {
        'product_name': product_name_receive,
        'price': price_receive,
        'image': image_receive,
        'link': link_receive,
        'story': story_receive,
        'user_id': user_id_receive,
    }
    
    db.gifts.insert_one(gift)
    return jsonify({'result': 'success', 'msg': '선물이 등록되었습니다.'})

@app.route('/giftprofile')
def gift_page():
    return render_template('gift.html')

@app.route('/yourgiftprofile', methods=['GET'])
def read_owner():
    user_receive = request.args.get('user_give')
    owners = list(db.profiles.find({'_id':ObjectId(user_receive)}, {'_id': False, 'password': False}))
    # print(profiles[0])
    # ObjectId(string_id_from_front)
    # print(db.profiles.find_one({"_id": ObjectId(profiles[0]['_id'])}))
    # 아이디 가져다쓰는...그런거...
    return jsonify({'result': 'success', 'owners': owners})

@app.route('/yourgiftlist', methods=['GET'])
def read_gift():
    user_receive = request.args.get('user_give')
    gifts = list(db.gifts.find({'user_id':user_receive}, {'_id': False}))
    # print(profiles[0])
    # ObjectId(string_id_from_front)
    # print(db.profiles.find_one({"_id": ObjectId(profiles[0]['_id'])}))
    # 아이디 가져다쓰는...그런거...
    return jsonify({'result': 'success', 'gifts': gifts})

# @app.route('/giftlist', methods=['GET'])
# def read_profile():
#     profiles = list(db.profiles.find({},{'_id':0}))
#     return jsonify({'result': 'success', 'profiles': profiles})

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)