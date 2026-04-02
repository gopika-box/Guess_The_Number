from flask import Flask,render_template, request,session, redirect,url_for
import random
app=Flask(__name__)
#for session
app.secret_key="your_secret_key"

@app.route('/')
def home():
    #if game not started;start
    if "number" not in session:
        session['max']=50
        session['number']=random.randint(1,session['max'])
        session['attempts']=0
    return render_template("index.html",level=session.get("level","easy"))

@app.route('/set_difficulty',methods=['POST'])
def set_difficulty():
    lvl = request.form.get("lvl")
    if lvl=="easy":
        max=50
    elif lvl =="medium":
        max=100
    elif lvl=='hard':
        max=500
    session['max']=max
    session['number']=random.randint(1,max)
    session['attempts']=0
    session['level']=lvl

    return redirect(url_for('home'))
    

@app.route('/guess', methods=["POST"])
def guess():
    user_guess = int(request.form.get("guess"))

    real_num = session['number']
    attempts=session['attempts']
    #increase attempt
    attempts+=1
    session['attempts']=attempts

    #compare logic
    if user_guess < real_num:
        msg="TOO LOW"
    elif user_guess> real_num:
        msg="TOO HIGH"
    else:
        msg="YAY! YOU GOT IT"
        return render_template('index.html',message=msg,attempts=attempts,win=True)

    return render_template("index.html",message=msg,attempts=attempts)

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("home"))
if __name__ =="__main__":
    app.run()