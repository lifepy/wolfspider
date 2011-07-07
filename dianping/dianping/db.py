import pymongo

whaleshark = '128.210.189.88'
vega = '204.62.14.55'
def get_connection():
    conn = pymongo.Connection(vega).dianping
    conn.authenticate('dianping','crawler')
    return conn
