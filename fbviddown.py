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

import requests
import re
import urllib
import os,time
import engine

#https://www.facebook.com/519691891892331/videos/2354691294789484/

def part2(link):
    parse = urllib.parse.urlparse(link).path.split('/')
    dName = '{0}-{1}-{2}.mp4'.format(parse[1],parse[2],parse[3])
    dPath = 'D:\\Download'
    print(os.path.join(dName, dPath))
    
    html = requests.get(link)
    
    try:
        url = re.search('hd_src:"(.+?)"', html.text)[1]
        print('High Q')
    except:
        url = re.search('sd_src:"(.+?)"', html.text)[1]
        print('Normal Q')
        
        
    response = requests.get(url, stream=True)

    video = engine.Stream(url, dPath, dName)
    video.download()
    
lst = []

while True:
    link = input('Link :')
    if link == 'exit':
        break
    else:
        lst.append(link)
    

for lnk in lst: 
    part2(lnk)
