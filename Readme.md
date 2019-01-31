# Namma BLR

Namma Blr is a cloud-enabled, mobile-ready, Flask powered app to manage Garbage Collection in Bangalore.

  - As an user, upload areas which you'd like to see cleaned up
  - As an admin, manage areas uploaded and resolve issues
  - Magic

You can also:
  - Make an account and monitor your requests
  - See statistics of frequency of requests of different areas in Bangalore


### Tech

Namma Blr uses a number of Frameworks, APIs and Languages to work properly:

* Flask - Python Miniframework to make and deploy web apps
* Visual Studio - An awesome text editor by Microsoft
* Google Maps API - An API to use Map features within your app
* Heroku - A free site to host your Web apps
* Pyrebase - Framework to use Firebase through python
* Bootstrap - Template for pretty css
* Jinja2 - HTML templating engine
* FontAwesome - Amazing fonts by Google
* jQuery - Javascript framework to automate client side scripting

And of course Namma Blr itself is open source with a [public repository](https://github.com/DevangJ/nammablr)
 on GitHub.

### Installation

Namma Blr requires [Python 3.7.2](https://www.python.org/downloads/) to run.

Namma Blr is already live on Heroku.
* [Admin App](https://nammablr.herokuapp.com/aa)
* [User App](https://nammablr.herokuapp.com/ua)

If you wish to run the app locally you can clone from the [repository](https://github.com/DevangJ/nammablr)

Set up the virtual environment and install the dependencies and start the server.

```sh
$ cd nammablr
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python app.py
```

Your instance of the app will be running on
> 0.0.0.0:8000/