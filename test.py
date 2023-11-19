from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def test():
   if request.method == 'POST':
      uname = request.form['uname']
      psw = request.form['psw']
      return render_template('display.html', username=uname,password=psw)
   else:
        return render_template('login.html')