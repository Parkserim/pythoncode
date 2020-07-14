#REQUEST.METHOD

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/method/',methods=['GET','POST'])
def login():
    if request.method == "POST":
        return "Post"
    else:
        return "Get"


#REQUEST.ARGS

#http://127.0.0.1:8089/login?name1=serim
@app.route('/login')
def login1():
    user = request.args.get('name1')
    return 'User %s'%user

@app.route('/login',methods=['POST'])
def login2():
    username = request.form['username']
    pw = request.form['password']  #request.form = 딕셔너륑~
    return 'Username : %s, pw : %s'%(username,pw)

if __name__ == '__main__':
    app.run(debug=True,port=8089)