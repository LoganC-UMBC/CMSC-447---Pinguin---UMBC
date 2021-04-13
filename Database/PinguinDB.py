# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:44:20 2021

@author: Sam
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:46:40 2021

@author: Sam
"""

import pymongo, datetime, time

from bson.objectid import ObjectId
from class_user import User
from random import seed, randint
from coolname import generate_slug


import names


class PinguinDB:
    
    # commented out self.client is for guest DB access role instead of admin DB access
    def __init__(self):
        self.user = User()
        self.client = pymongo.MongoClient("mongodb+srv://PinguinAdmin:D47b5PIrtJxIhnuV@pinguin-cluster.vvukk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        #self.client = pymongo.MongoClient("mongodb+srv://guest:kYmIc3X8vSHcNTfy@pinguin-cluster.vvukk.mongodb.net/Pinguin?retryWrites=true&w=majority")
        self.db = self.client.Pinguin
        self.groups = self.client.Groups
        self.users = self.client.Users
        self.invites = self.client.Invites
        self.forums = self.client.Forums
        self.calendars = self.client.Calendar
        self.documents = self.client.Documents
        self.tasks = self.client.Tasks
        
        self.usersOld = self.db.Users
        self.groupsOld = self.db.Groups
       
    
    
    
    # changes default user credentials
    def change_user(self, user_id, name, pword, _id):
        self.user.user_id = user_id
        self.user.name = name
        self.user.pword = pword
        self.user._id = _id
        return 1
    
    # will check 
    def login(self, user_id, pword):
        if(self.usersOld.count_documents({'user_id': user_id} and {'pass':pword})):
            print("login successful")
            user_doc =  self.usersOld.find_one({'user_id':user_id} and {'pass':pword})
            self.change_user(user_doc['user_id'], user_doc['name'], user_doc['pass'], user_doc['_id'])
            return 1
        else:
            print('login unsucessful')
            return 0



    def create_account(self, user_id, pword, name):
        if(self.usersOld.find_one('user')):
            return 0
        else:
            self.user.user_id = user_id
            self.user.pword = pword
            self.user.name = name
            
            user_account = {"user_id": self.user.user_id,
                            "name": self.user.name,
                            "pass": self.user.pword,
                            "role":"user",
                            "groups":[]}
            
            self.usersOld.insert_one(user_account)
            
            self.user._id = self.usersOld.find_one({"user_id":self.user.user_id}).get("_id")
            
            return 1
        
    def create_group(self, name, description, invites):
        
        invites_split = invites.split(",")
        
        group_post = {"name": name,
                      "owner":self.user.name,
                      "description":description,
                      "invites": invites_split,
                      "members":[self.user.user_id]}
        
        self.db.Groups.insert_one(group_post)


    def testConnections(self):
        print(self.db.list_collection_names())



    def get_groups(self):
        if (self.user.name != 'guest'):
            return 0


        else:
            docs = self.users.find_one({'_id':self.user.user_id})
            if(docs != None):    
                group_count = 0
            #print(docs)
            # for groups in docs[0]['groups']:
            #     group_count += 1
            #     print(groups)
                
            # for key in cursor:
            #     for data in key :
            #         print(key[data])

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
    
    
    def group_create(self, group_name, group_users):
        if(group_users != None):
            group = {'group_name':group_name,
                     'owner':self.user._id,
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
    def errorHandler(self,error):
        
        return

    def create_many_accounts(self,men, women):
        seed(time.time())
        
        for man in range(men):
            name = names.get_first_name(gender='male')
            number = str(randint(100, 999))
            pword = "pinguin"
            user_id = name+number+"@gmail.com"
            self.create_account(user_id, pword, name)

        for woman in range(women):
            name = names.get_first_name(gender='female')
            number = str(randint(100, 999))
            pword = "pinguin"
            user_id = name+number+"@gmail.com"
            self.create_account(user_id, pword, name)
    
    def create_emails(self,num):
        seed(time.time())
        invites = ""
        for x in range(num):
            if(x%2 == 0):
                name = names.get_first_name(gender='male')
                invite = name+"@gmail.com,"
                    
            else:
                name = names.get_first_name(gender='female')
                invite = name+"@gmail.com,"
            
            invites += invite
        # print(invites)
        return invites
        
    def create_many_groups(self, group_num):
        seed(time.time())
        for i in range(group_num):
            group_name = generate_slug(3)
            invites = self.create_emails(6)
            self.create_group(group_name, "Test Description", invites)

x = PinguinDB()

x.login("s99@umbc.edu","princess")
x.create_emails(2)
x.create_many_groups(3)

#x.create_many_accounts(1,1)

#x.get_groups()
#x.create_account("s99@umbc.edu","princess","sam")
# x.change_login('penny', 'PinguinTizeMeCapn')
# x.group_create('Pinguin Party',['polly', 'poppy','piety','perry','phoebe'] )
# print(x.db.Groups.count_documents({}))
# x.change_login('sam', 'princess')
# print(x.user.name)
# print(x.send_invites(['penny', 'polly', 'poppy','piety','perry','phoebe']))
# x.testConnections()

#x.send_post('Pinguin Party',"This group is for planning and having a party!")
