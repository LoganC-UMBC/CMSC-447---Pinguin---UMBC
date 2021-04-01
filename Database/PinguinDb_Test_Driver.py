# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:29:37 2021

@author: Sam
"""


import pymongo

client = pymongo.MongoClient("mongodb+srv://PinguinAdmin:D47b5PIrtJxIhnuV@pinguin-cluster.vvukk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
print(client.list_database_names())

db = client.Pinguin
print(db.list_collection_names())
