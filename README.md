# Fish 

![Fish](https://i.imgur.com/nQ45dEy.png "Fish")
![Downloads](https://img.shields.io/github/downloads/aarav2you/Fish/total?branch=master&label=Downloads&logo=GitHub&logoColorr=ffffff&labelColor=282828&color=informational&style=flat)
![Forks](https://img.shields.io/github/forks/aarav2you/Fish?branch=master&label=Forks&logo=GitHub&logoColor=ffffff&labelColor=282828&color=informational&style=flat)
[![GitHub repo size](https://img.shields.io/github/repo-size/aarav2you/Fish?branch=master&label=Repo%20Size&logo=GitHub&logoColor=ffffff&labelColor=282828&style=flat)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Discord](https://img.shields.io/discord/815516003034857522?label=Discord&logo=discord&logoColor=ffffff&labelColor=7289DA&color=2c2f33)

## Note: This project will no longer be developed any further due to reasons in real life, however pull requests are welcome and I will still be reviewing them.
## About
Fish is a phishing tool that inhabits a collection of webpages. It tries to replicate webpages as closely as possible for a hard to distinguish phishing page.
## Features
- Up-to-date login phishing page.
- Easily configurable, with a startup script.
- Has a menu that can be used to select the different sites (with color!).
- Can use any domain including but not limited to `Ngrok`, `Freenom`, `GoDaddy` etc.
- Has built-in option to install and use ngrok for a free public domain.
- Uses flask. Has options in the start-up script to configure the host and port.


## Installation 
#### Clone the repo:
`$ git clone https://github.com/aarav2you/Fish.git`


------------

#### Go into the repo:
`$ cd Fish/`

------------

#### Run fish.py
`$ pip install -r requirements.txt`

`$ python fish.py`

------------

## Great! How do I use it?
You can specify the values it asks for when executing the `app.py`. Leaving the settings on default is the best option (just press ⏎). Refer to the table below for all values:

| `Enter redirect URL` | The link it will redirect the victim to after credentials have been logged in `credentials.log`. `Default: https://www.office.com/?auth=2` 	|
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `Flask server host`  | The local IP your flask server will run on. `Default: 127.0.0.1`                                                                    |
| `Flask server port`  | The port your flask server will run on. `Default: 80`                                                                               |
| `Use ngrok`          | This uses `nGrok`to to forward the phishing page to a public domain. More on this [here][1]. `Default: n`                           |                        	
## Legal
Usage of `Fish` for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes. White hat hackers, best of luck, make sure you have consent!

## Contribution
We have built this with our ❤️. If you would like to contribute, please read [how to contribute/contributing guidelines](https://github.com/aarav2you/Fish/blob/dev/CONTRIBUTING.md). If you would like to suggest, please open an issue with the label **Enhancement**.

## Authors
Made lovingly by [aarav2you][3] and [Kritagyaispro][4] and others who contributed!

## Issues
[![GitHub Issues](https://img.shields.io/github/issues/aarav2you/Fish?branch=master&label=Issues&logo=GitHub&logoColor=ffffff&labelColor=282828&style=flat)]()
[![GitHub Closed Issues](https://img.shields.io/github/issues-closed/aarav2you/Fish?branch=master&label=Closed%20Issues&logo=GitHub&logoColor=ffffff&labelColor=282828&style=flat)]()
[![GitHub Issues](https://img.shields.io/github/issues/aarav2you/Fish?branch=master&label=Issues&logo=GitHub&logoColor=ffffff&labelColor=282828&color=informational&style=flat)]()


[1]: https://ngrok.com "here"
[2]: https://github.com/aarav2you/Fish/tree/dev "Dev"
[3]: https://github.com/aarav2you "aarav2you"
[4]: https://github.com/Kritagyaispro "Kritagyaispro"
