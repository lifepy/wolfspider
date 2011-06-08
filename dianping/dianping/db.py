import pymongo

def get_connection():
    conn = pymongo.Connection().dianping
    conn.authenticate('dianping','crawler')
    return conn

