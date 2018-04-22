#-*-coding:utf-8-*-
##frame模式
# from flask import Flask,request
#
# app=Flask(__name__)
#
# @app.route('/',methods=['GET','POST'])
# def home():
#     return '<h1>home</h1>'
#
# @app.route('/signin',methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
#
# @app.route('/signin',methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='123':
#         return '<h3>hello admin!</h3>'
#     return '<h3>bad username or password.</h3>'
#
#
# if __name__ == '__main__':
#     app.run()

#模板MVC
from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='123':
        return render_template('signinok.html',username=username)
    return render_template('form.html',message='登录名或密码错误',username=username)

if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
=======
    app.run()
>>>>>>> 7bdc3e4d0424112eccdbd3565a53d77903206080
