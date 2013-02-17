import pymongo
import cgi
import re
import datetime
import random
import hmac
import user
import sys

connection_string = "mongodb://localhost"

#remove orphan images
def remove():
    connection = pymongo.Connection(connection_string, safe=True)

    db = connection.blog
    images = db.images
    albums = db.albums
    l =[]
    try:
        for i in images.find():
            if albums.find({"images":i["_id"]}).count() == 0:
                images.remove({"_id":i["_id"]})

#        print len(l)

    except:
        print "Unexpected error:", sys.exc_info()[0]


if __name__ == '__main__':
    remove()
