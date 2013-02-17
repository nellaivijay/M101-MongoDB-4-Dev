from bson.son import SON
import pymongo
import sys

#connection
conn = pymongo.Connection("mongodb://localhost", safe=True)

db = conn.school
students = db.students

def update_data():
    data_filter = {'_id':True, 'scores':True}

    cursor = students.find({}, data_filter).sort([('_id',pymongo.ASCENDING)])

    dic = {}
    removed = []

    for c in cursor:
        cid = c['_id']
        current = 10000
        for s in c['scores']:
            if s['type'] == 'homework' and s['score'] <= current:
                current = s['score']
#removed.append(current)    
        c['scores'].remove({'type': 'homework', 'score': current})
        students.update({'_id': cid},{'$set':{'scores': c['scores']}})

#    print len(removed)

update_data()
