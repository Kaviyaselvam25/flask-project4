from flask import Flask, render_template ,request
app=Flask(__name__)
#routing--1st page
@app.route("/")
def home():
    return render_template("login2.html")
#routing "/login"-login page
#database: username/password
database={'Ravi':'1234',"Kaviya":'kaviya','Reena':'KAVIYA','rinthiya':'RIN@123'}
@app.route('/form_login' ,methods=['POST','GET'])
def form_login():
    if request.method=='POST':
        name1=request.form['username']#example--Selvam#Reena#Reena
        password1=request.form['password']#password--kaviya#kaviya#KAVIYA
        if name1 not in database:
            return render_template('login2.html',info="Invalid User")
        else:
            if database[name1]!=password1:
                return render_template('login2.html',info='Invalid Password')
            else:
                return render_template('home2.html', name=name1)
    return render_template('login2.html')
#main program
if __name__=='__main__':
    app.run(debug=True)

