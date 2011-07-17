from .. import db
from db import get_connection
import gridfs

db = get_connection()
fs = gridfs.GridFS(db, collection='images')

for img in db.images.files.find():
    if db.images.files.find({'url':img['url']}).count() > 1:
        print "DELETING: " + img['filename']
        fs.delete(img['_id'])
