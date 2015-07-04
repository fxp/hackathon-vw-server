# -*- coding: UTF-8 -*-

__author__ = "MeoWoodie"

from flask import Flask, render_template, url_for
import json


app = Flask(__name__)

@app.before_first_request
def init_before_first_request():
    pass

@app.route("/trace/")
@app.route("/trace/<navid>/", methods=["GET"])
def trace(navid=None):
    # Analyse the incoming data.
    # data = json.loads(request.data)

    # result = json.dumps({"result": navid, "code": 0})
    return render_template("trace.html", navid=navid)

@app.route("/test/", methods=["POST"])
def test():
    # Analyse the incoming data.
    # data = json.loads(request.data)

    result = json.dumps({"result": "test", "code": 0})
    print result
    return result

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9010)
