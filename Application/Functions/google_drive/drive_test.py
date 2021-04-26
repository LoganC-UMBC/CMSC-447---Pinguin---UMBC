from pydrive.auth import GoogleAuth
#Authorizes google drive access

def driveAuthentic():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
    gauth.SaveCredentialsFile("mycred.txt") #saves credentials to a file
    drive = GogleDrive(gauth)
    return drive 

def create(user_title, user_content):
    userfile= drive.CreateFile({'title': user_title})
    userfile.SetContentString(user_content)
    userfile.Upload()
    return userfile

def list_of_files():
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))


def download_files(download_title):
    file_list = drive.ListFile({'q': "title = " +str(user_title)+ "and trashed = false"}).GetList()
    print(file_list[0]['title'])
    file_id = file_list[0]['id']

    file = drive.CreateFile({'id':file_id})
    file.GetContentFile(download_title)

def trash_files(files):
    files.Trash()

def update_title(files, user_title,new_title):
    files[user_title] = new_title
    files.upload
    return files

def update_content(files):
    files.SetContentString(user_content)
    files.Upload
    return files







#variables
#user_title
#user_content
#download_title

