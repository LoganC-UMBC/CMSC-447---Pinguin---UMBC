from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#Authorizes google drive access


class Google_Drive(object):
    def __init__(self, auth):
        self.drive = GoogleDrive(auth)

    #create file
    def create(self, user_title):
        user_file = self.drive.CreateFile({'title': user_title})
        user_file.Upload()


    def trash_files(self, file_title):
        # find the file with this name
        file_list = self.drive.ListFile({'q': "title = '%s' and trashed = false" % file_title}).GetList()
        # delete the first occurance of this file
        file_list[0].Trash()


"""auth = GoogleAuth()
auth.LocalWebserverAuth()
auth.SaveCredentialsFile("mycred.txt")  # Saves credentials to a file
d = Google_Drive(auth)
d.create("my file")"""