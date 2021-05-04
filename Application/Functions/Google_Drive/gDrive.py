from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#Authorizes google drive access


class Google_Drive(object):
    def __init__(self, auth):
        self.drive = GoogleDrive(auth)

    #create file
    def create(self, user_title):
        user_file = self.drive.CreateFile({'mimeType': 'application/vnd.google-apps.document', 'title': user_title})
        print(user_file)
        user_file.Upload()
        print(user_file)
        return user_file['alternateLink']


    def trash_files(self, file_title):
        # find the file with this name
        file_list = self.drive.ListFile({'q': "title = '%s' and trashed = false" % file_title}).GetList()
        # delete the first occurance of this file
        file_list[0].Trash()


auth = GoogleAuth()

auth.LocalWebserverAuth()
d = Google_Drive(auth)
#auth.SaveCredentialsFile("mycred.txt")  # Saves credentials to a file

print(d.create("my file"))