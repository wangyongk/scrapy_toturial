#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students2
collection = db['students2']
student2 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = collection.insert(student2)
print(result)