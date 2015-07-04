from string import strip
import pymongo

__author__ = 'Jayvee'


def get_android_trace_list(navid, vw_android_conn):
    vw_android = vw_android_conn
    navid = strip(navid)
    find_result = vw_android.find({'navid': navid})
    result_list = []
    # ddd = vw_android.find_one()
    # print ddd
    for trace in find_result:
        result_list.append(
            {'x': trace['x'], 'y': trace['y'], 'v': trace['v'], 'd': trace['d'], 'dayid': trace['dayid']})
    # print result_list
    return result_list


def get_ios_trace_list(navid, vw_ios_conn):
    vw_ios = vw_ios_conn
    find_result = vw_ios.find({'navid': navid})
    result_list = []
    for trace in find_result:
        result_list.append({'x': trace['x'], 'y': trace['y'], 'v': trace['v'], 'd': trace['d']})
    # print result_list
    return result_list


if __name__ == '__main__':
    conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
    rootDB = conn.Hackathon
    vw_android_db = rootDB.vw_android
    tracelist = get_android_trace_list('1403804539139', vw_android_db)
    # for trace in tracelist:
    #     print trace
    print len(tracelist)
