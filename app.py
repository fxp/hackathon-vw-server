# -*- coding: UTF-8 -*-

__author__ = "MeoWoodie"
import pymongo
import MongoUtils
from flask import Flask, render_template, request
import json


app = Flask(__name__)

conn = pymongo.MongoClient(host='192.168.1.182', port=27017)
rootDB = conn.Hackathon
vw_android_db = rootDB.vw_android

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

@app.route("/story/")
@app.route("/story/<navid>/", methods=["GET"])
def story(navid):
    # Analyse the incoming data.
    # data = json.loads(request.data)

    # result = json.dumps({"result": navid, "code": 0})
    return render_template("story.html", navid=navid)

@app.route("/test/", methods=["POST"])
def test():
    # Analyse the incoming data.
    data = json.loads(request.data)

    result = json.dumps({"result": data, "code": 0})
    return result

@app.route('/tracelist/', methods=['POST'])
def tracelist():
    # print request.get_data()
    try:
        post_data = json.loads(request.data)
        navid = post_data['navid']
        tracelist = MongoUtils.get_android_trace_list(navid, vw_android_db)
        print len(tracelist)
        return json.dumps({'status': 'ok', 'tracelist': tracelist})
    except Exception, e:
        return {'status': 'error', 'msg': e}

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9010)
