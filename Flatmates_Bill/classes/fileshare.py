from filestack import Client

class FileShare:

    def __init__(self,filepath,api = 'provide api key to upload file, store in cloud'):
        self.filepath = filepath
        self.api = api
    
    def getUrl(self):
        client = Client(self.api)
        file_link = client.upload(self.filepath)        
        return file_link.url