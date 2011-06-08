import pymongo

whaleshark = '128.210.189.88'
def get_connection():
    conn = pymongo.Connection(whaleshark).dianping
    conn.authenticate('dianping','crawler')
    return conn

