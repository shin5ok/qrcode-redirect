from flask import *
import os
import myutil

APIKEY = os.environ.get('BITLY_APIKEY')

app = Flask(__name__)

@app.route("/")
def _root():
    return render_template("index.html")

@app.route("/gen",methods=['POST'])
def _gen():
    url = request.form["url"]
    params = myutil.gen(APIKEY, url)
    return render_template("gen.html", params=params)

if __name__ == '__main__':
    app.run()