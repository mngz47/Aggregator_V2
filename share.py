
import requests

import facebook

class share():

    def send(self,title,text,link):
        ff = facebook()
        ff.__init__('app_id','app_secrete','fp_page_id')
        return ("<br>Post On FaceBook: "+ff.post_to_fb(title+text,link))
