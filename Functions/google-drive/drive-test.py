from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def drive_authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
    gauth.SaveCredentialsFile("mycred.txt") # Saves credentials to a file
    drive = GoogleDrive(gauth)
    return drive

# create a file
def drive_create(drive, user_title):
    user_file = drive.CreateFile({'title': user_title})
    user_file.Upload()

# delete a file
def drive_delete(drive, file_title):
    # find the file with this name
    file_list = drive.ListFile({'q': "title = '%s' and trashed = false" % file_title}).GetList()
    # delete the first occurance of this file
    file_list[0].Trash()

# TESTING
drive = authenticate()
#create(drive, "my file")
trash_files(drive, "my file")