
import requests
import settings
import os


class FaceBook:
    token = ""
    fb_page_id = ""
    
    
    def __init__(self, app_id, app_secret,fp_page_id):
        self.token = self.get_fb_token(app_id, app_secret)
        self.fb_page_id = fb_page_id
        print(self.token)

    def get_fb_token(self, app_id, app_secret):
        url = 'https://graph.facebook.com/oauth/access_token'
        payload = {
            'grant_type': 'client_credentials',
            'client_id': app_id,
            'client_secret': app_secret
        }
        response = requests.post(url, params=payload)
        personal = response.json()['access_token']
        params = {
            "fields": personal
        }
        r = requests.get(
            "https://graph.facebook.com/" + self.fb_page_id + "?fields=access_token&access_token=" + personal)
        print(r.text)
        return r.json()['access_token']

    def post_to_fb(self, desc, link):
        params = {
            "message": desc,
            "link": link,
            "access_token": self.token
        }
        r = requests.post("https://graph.facebook.com/v5.0/" + self.fb_page_id  + "/feed", data=params)
        return (r?"Succes":"failure")