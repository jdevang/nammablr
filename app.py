from flask import Flask, render_template, request, redirect, session, url_for
import pyrebase # For firebase connectivity

config = {
    "apiKey": "AIzaSyCOvJ2dzgqiA-Cq5LHP7wgrEj34WbMGE_Q",
    "authDomain": "vcast-record-keeping.firebaseapp.com",
    "databaseURL": "https://vcast-record-keeping.firebaseio.com",
    "storageBucket": "vcast-record-keeping.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)
app.secret_key = 'vcastsecretkey'


@app.route("/")
def main_page():
    return render_template("goto_resp_apps.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
