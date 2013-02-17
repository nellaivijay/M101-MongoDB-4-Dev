from bson.son import SON
import pymongo
import sys

#connection
conn = pymongo.Connection("mongodb://localhost", safe=True)

db = conn.students
grades = db.grades

def find():
    query = {'type':'homework'}
    group = {'$group':{'student_id'}}

    cursor = grades.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])

    removed = []
    dic = {}

    for c in cursor:
        if c["student_id"] not in dic:
            dic[c["student_id"]] = c["student_id"]
        else:
            removed.append(c["_id"])

    for i in removed:
        grades.remove({"_id" : i})

    print grades.count()
find()
