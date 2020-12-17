
import requests

import facebook

class share():

    def send(self,title,text,link):
        ff = facebook()
        ff.__init__('838292889616021','eb485dec6fac405b62e666929f03d272','195349390839130')
        return ("<br>Post On FaceBook: "+ff.post_to_fb(title+text,link))
