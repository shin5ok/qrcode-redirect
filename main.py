from flask import *
import myutil

app = Flask(__name__)

@app.route("/")
def _root():
    return render_template("index.html")

@app.route("/gen",methods=['POST'])
def _gen():
    url = request.form["url"]
    params = myutil.gen(url)
    print(params)
    return render_template("gen.html", params=params)


if __name__ == '__main__':
    app.run()