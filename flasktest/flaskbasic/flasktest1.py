#Flask 웹 어플리케이션 기본 골격

from flask import Flask,render_template
from flask.globals import request
request
app = Flask(__name__) #현재파일의 파일명

@app.route('/')  #root
def index():
    return render_template('index.html')

#http://127.0.0.1:8089/cakes
@app.route('/cakes')  
def cakes():
    return "Yummy cakes!"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s'%username

#http://127.0.0.1:8089/user/serim/23
@app.route('/user/<username>/<int:age>')  
def show_user_profile_age(username,age):
    return 'Username %s, 나이 %d'%(username,age)


if __name__=='__main__':
    app.run(debug=True,port=8089)  #디버그=자동 새로고침 / 기본=5000

