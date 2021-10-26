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
    print(request.form)
    url = request.form["url"]
    print(APIKEY)
    params = myutil.gen(APIKEY, url)
    print(params)
    return render_template("gen.html", params=params)

if __name__ == '__main__':
    app.run()
