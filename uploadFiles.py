import os
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFiles(file_from):
      dbx = dropbox.Dropbox(self.access_token)
      for root,dirs,files in os.walk(file_from):
          relative_path = os.path.relpath(local_path,file_from)
          dropbox_path = os.path.join(file_to,relative_path)
          with open(local_path,'rb') as f:
              dbx.files.upload(f.read(),dropbox.path,mode=WriteMode('overwrite'))
    
def main():
    access_token = "sl.Av5Prtlu_maoy87pC3qtzS6oNKWVMHUofLqP01EZmLsGdE46TS6jh6L9Hoiyg1NTLI0GFQD-IO3_kfV4CMYity8yJoZpOk2d4xtysofBMphxEE205BgczDu4ZFGpb0cJFIDm5ck"
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to transfer to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved successfully")