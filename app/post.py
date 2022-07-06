
import requests

class post():

   
    def send(self,title,text,categories):
    
            url = "https://api.medium.com/v1/users/2b586e990c6c6e0328bde9b5a758d06b7bbab7221e4e6d5e237844dbbb7caf307/posts"
            data = {
            "title": title,
            "contentFormat": "html",
            "content": text,
            "tags": categories.split(','),
            "publishStatus": "public"
            }
            s = requests.Session()
            return s.post(url, data=data)
        
       
        