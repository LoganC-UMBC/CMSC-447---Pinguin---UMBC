# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:46:40 2021

@author: Sam
"""

import pymongo
import datetime
from class_user import User


class PinguinDB:
    
    # commented out self.client is for guest DB access role instead of admin DB access
    def __init__(self):
        self.user = User()
        self.client = pymongo.MongoClient("mongodb+srv://PinguinAdmin:D47b5PIrtJxIhnuV@pinguin-cluster.vvukk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        #self.client = pymongo.MongoClient("mongodb+srv://guest:kYmIc3X8vSHcNTfy@pinguin-cluster.vvukk.mongodb.net/Pinguin?retryWrites=true&w=majority")
        self.db = self.client.Pinguin
        self.users = self.db.Users
    
    # changes default user credentials
    def change_user(self, name, pword):
        self.user.name = name
        self.user.pword = pword
        return
    
    # will check 
    def login(self, user, pword):
        if(self.users.count_documents({'user': user} and {'pass':pword})):
            print("login successful")
            return 1
        else:
            print('login unsucessful')
            return 0
        
    def create_account(self, user, pword):
        if(self.users.find_one('user')):
            return 0
        else:
            return 1
        
        
    def testConnections(self):
        print(self.db.list_collection_names())
        
    def get_groups(self):
        if (self.user.name != 'guest'):
            return
        
    # Refresh handlers

    def refresh_tasks(self):
        return
    
# going to need to figure out to send these back in order
    def refresh_forum(self):
        
        return

    def refresh_calendar(self):
        return
    
    def refresh_group_invites(self):
        return

    def refresh_all(self):
        return
    
    def calendar_add(self):
        return
    
    #take a list of usernames to parse deliminate on ','
    #add to group 
    def group_create(self, group_name, group_users):
        if(group_users != None):
            group = {'group_name':group_name,
                     'owner':self.user.name,
                     'users':[user for user in group_users]
                     }
            group['users'].append(self.user.name)
            
        else:
            group = {'group_name':group_name,
                     'owner':self.user.name,
                     'users':'None'
                     }
        self.db.Groups.insert_one(group)
        return 1

    def send_invites(self, invites):
        post = {'sender':self.user.name,
                'receivers': [user for user in invites]
                }
        return 1
    
    # Forums Window
    
    def receive_invites(self):
    
        return
    
    
    def send_post(self, group, message):
        post = {'author':self.user.name,
                'group':group,
                'message':message,
                'date':datetime.datetime.utcnow()
                }
        
        self.db.Forums.insert_one(post)
        return 1
    
    def receive_posts(self):
        return 
    
    # Error Management
    def errorHandler(error):
        return
                

x = PinguinDB()
# x.change_login('penny', 'PinguinTizeMeCapn')
# x.group_create('Pinguin Party',['polly', 'poppy','piety','perry','phoebe'] )
# print(x.db.Groups.count_documents({}))
# x.change_login('sam', 'princess')
# print(x.user.name)
# print(x.send_invites(['penny', 'polly', 'poppy','piety','perry','phoebe']))
# x.testConnections()

x.send_post('Pinguin Party',"This group is for planning and having a party!")
