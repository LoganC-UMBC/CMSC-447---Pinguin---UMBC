from pydrive.auth import GoogleAuth
#Authorizes google drive access



def authenticate ():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
    #gauth.SaveCredentialsFile("mycred.txt") #saves credentials to a file
    drive = GoogleDrive(gauth)

#create file
def create(user_title):

    user_file = drive.CreateFile({'title': user_title})
    user_file.Upload()


def trash_files(trash_file):
    #creates an instance of the file
    file2 = drive.CreateFile({'title': trash_file})
    #puts file into trash folder
    file2.Trash()


