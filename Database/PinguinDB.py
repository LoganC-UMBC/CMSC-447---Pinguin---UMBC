import pymongo, datetime, time, hashlib

from bson.objectid import ObjectId
from Database.utils.class_user import User
from random import seed, randint





class PinguinDB:
    
    # commented out self.client is for guest DB access role instead of admin DB access
    def __init__(self):
        self.user = User()
        self.client = pymongo.MongoClient("mongodb+srv://PinguinAdmin:D47b5PIrtJxIhnuV@pinguin-cluster.vvukk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        #self.client = pymongo.MongoClient("mongodb+srv://guest:kYmIc3X8vSHcNTfy@pinguin-cluster.vvukk.mongodb.net/Pinguin?retryWrites=true&w=majority")
        
        self.groups = self.client.Groups.Pinguin
        self.users = self.client.Users.Pinguin
        self.invites = self.client.Invites
        self.forums = self.client.Forums
        self.calendars = self.client.Calendar
        self.documents = self.client.Documents
        self.tasks = self.client.Tasks
        
        self.db = self.client.Pinguin
        self.usersOld = self.db.Users
        self.groupsOld = self.db.Groups
       
    
    
    
    # changes default user credentials
    def change_user(self, user_id, name, pword, _id, groups):
        self.user.user_id = user_id
        self.user.name = name
        self.user.pword = pword
        self.user._id = _id
        self.user.groups = groups
        return 1
    
    # will check 
    def login(self, user_id, pword):
        m = hashlib.sha256(pword.encode())
        if(self.users.count_documents({'user_id': user_id} and {'pass':m.hexdigest()})):
            user_doc =  self.users.find_one({'user_id':user_id} and {'pass':m.hexdigest()})
            self.change_user(user_doc['user_id'], user_doc['name'], user_doc['pass'], user_doc['_id'], user_doc['groups'])
            print("login successful")
            
            if(len(self.user.groups) >= 1):
                self.user.defaultGroup = self.user.groups[0]
            return 1
        else:
            print('login unsucessful')
            return 0

    def current_user(self):
        userList = []
        userList.append(self.user._id)
        userList.append(self.user.user_id)
        userList.append(self.user.name)

        return userList
        
    #def change_group(self, group_name):
        #if(self.users.find_one({"groups":group_name})):
            #self.user

    def create_account(self, user_id, pword, name):
        if(self.users.find_one({"user_id":user_id})):
            print('User already exists')
            return 0
        else:
            self.user.user_id = user_id
            m = hashlib.sha256(pword.encode())
            self.user.pword = m.hexdigest()
            self.user.name = name
            
            user_account = {"user_id": self.user.user_id,
                            "name": self.user.name,
                            "pass": self.user.pword,
                            "role":"user",
                            "groups":[]}
            
            self.users.insert_one(user_account)
            
            self.user._id = self.users.find_one({"user_id":self.user.user_id}).get("_id")
            
            return 1
        
    def create_group(self, name, description):
        if(self.groups.find_one({"name":name})):
            print('Group of that name already exists')
            return 0
        else:
            #invites_split = invites.split(",")
            #"invites": invites_split,
            group_post = {"name": name,
                          "owner":self.user.name,
                          "description":description,  
                          "members":[self.user.user_id]}
        
            self.groups.insert_one(group_post)

            self.forums[name]


    def testConnections(self):
        print(self.db.list_collection_names())



    def get_groups(self):
        groupList = []
        for x in self.groups.find():
            if x.get("name") in self.user.groups:
                groupList.append(x)
                print(x)
        return groupList

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
        
        self.forums[group].insert_one(post)
        return 1
    
    def retrieve_all_posts(self, group):
        for x in self.forums[group].find():
            print(x)

    def calendar_add(self, group, description, date):
        
        calendarPost = {'author':self.user.name,
                        'group':group,
                        'day':date.day,
                        'month':date.month,
                        'year':date.year,
                        'description':description
                        }
        self.calendars[group].insert_one(calendarPost)

    def retrieve_calendar_posts(self, group, date, time):  

        if time == "month":
            for x in self.calendars[group].find({'month':date.month}):
                print("flag1")
                print(x)
        elif time == "year":
            for x in self.calendars[group].find({'year':date.year}):
                print(x)
        elif time == "day":
            for x in self.calendars[group].find({'day':date.day}):
                print(x)
        #not done, needs to diferentiate between month and year

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





