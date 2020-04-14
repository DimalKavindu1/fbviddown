#engine
#############################################################################
#                                                                           #
#           ===============================                                 #
#           Facebook Video Downloader v1.0                                  #
#           ===============================                                 #
#                                                                           #
#           Name : Fbviddown.py                                             #
#           Version : 1.0                                                   #
#           Autor : Dimal Kavindu                                           #
#           Date : 2020-01-08                                               #
#                                                                           #
#           Facebook Group - https://www.facebook.com/groups/SL.Coders      #
#           ------------------------------------------------------------    #
#           Join with us                                                    #
#                                                                           #
#               Youtube   - https://www.youtube.com/c/TesKill               #
#               Facebook  - https://www.facebook.com/TesKillEducation       #
#               Twitter   - https://www.twittr.com/TesKillEdu               #
#               Instagram - htttps://www.instagram.com/teskilleducation     #
#                                                                           #
#                                                                           #
#############################################################################

import urllib
import requests
import os, time
    
class Stream:
    def __init__(self, url, path, name):
        self.url = url
        self.path = path
        self.name = name
        self.response = requests.get(self.url, stream=True)
       
        self.total_length = int(self.response.headers.get('content-length'))
        self.start = 0
        self.end = 0
        self.t = 0

    def download(self):
        print('{0}Mb'.format(int(self.total_length)/1024**2))
        
        with open(os.path.join(self.path, self.name), 'wb') as f:
            if self.total_length is None:
                f.write(self.response.content)
            else:
                dl = 0
                chnk = int(self.total_length/100)
                for data in self.response.iter_content(chunk_size=chnk):

                    #calculate Duration
                    self.time_dur = time.time() - self.start
                    self.start = time.time()
                    
                    if self.time_dur == time.time():
                        self.time_dur = 0.000001
                    
                    
                    dl += len(data)
                    f.write(data)
                    
                    donedl = int((dl/self.total_length)*100)
                    
                    speed = (len(data)/1024)/self.time_dur
                    
                    print('{0}% - {1} kbps'.format(donedl,round(speed,3)))

