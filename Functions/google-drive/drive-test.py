from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
gauth.SaveCredentialsFile("mycred.txt")

drive = GogleDrive(gauth)

#variables
user_title
user_content
new_title


#to create doc and upload to user drive

file= drive.CreateFile({'title': 'Just Testing.txt'})
file.SetContentString("user content goes here")
file.Upload()


#To search for files, the following are possible commands
#trashed = true
#title contains ... and title contains ..
#title = ...

file_list = drive.ListFile({'q': "title contains 'user_title' and trashed = false" }).GetList()
print(file_list[0]['title']
file_id = file_list[0]['id'])

#downloading files as a local copy
file= drive.CreateFile({'id': file_id})
file.GetContentFile('title')


#sending local file to drive
new_title = drive.CreateFile()
new_title.SetContentFile('user_content)')




#create image file

    file2 = drive.CreateFile()
    file2.SetContentFile(user_content)
    file2.Upload()
    print('Created file %s with mimeType %s' % (file2['title'],
    file2['mimeType']))



 




