from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']
    ip = request.remote_addr
    #write data to file or to DB
    inputName = inputName.upper()+" hi!  Visiting from " + str(ip)
    return render_template("home.html",myName=inputName)
@app.route('/')
def home():
    
    return render_template("home.html",myName="")

@app.route('/serah/')
def seraht():
    return render_template("serah.html")

if __name__=="__main__":
    app.run(debug=True)
