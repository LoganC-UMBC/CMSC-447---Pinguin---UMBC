from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#Authorizes google drive access


class Google_Drive(object):
    def __init__(self, auth):
        self.drive = GoogleDrive(auth)

    def authenticate (self):
        #gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
        #gauth.SaveCredentialsFile("mycred.txt") #saves credentials to a file
        pass

    #create file
    def create(self, user_title):

        user_file = self.drive.CreateFile({'title': user_title})
        print(user_file)
        user_file.Upload()


    def trash_files(self, trash_file):
        #creates an instance of the file
        file2 = self.drive.CreateFile({'title': trash_file})
        #puts file into trash folder
        file2.Trash()
