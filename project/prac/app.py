from flask import Flask, render_template, 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['POST'])#포스트 요청만 받아라..?
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])#갯 요청만 받아라..?
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   {'result':'success', 'msg':'이 요청은 GET!'}
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

#@app.route('/mypage')
#def my_page():
#   return 'This my page!'

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)