# Version 0.1.1.beta

import browser_cookie3
import requests
import shutil
import re
import time

map_links = []

# DON'T FORGET TO CHANGE THIS FOLDER
with open("osumapdler\\map_links.txt") as f:
    map_links = f.read().splitlines()

print("Here are links to download:")
for l in map_links: print(l)

# importing login and password from browser
# change to '.chrome()' if you are signed in Chrome
cj = browser_cookie3.firefox()

# if these symbols are in the name of a beatmap they are replaced by '_'
notlist = ['*', '"', '/', '\\', ':', ';', '|', '?', '<', '>']

for url in map_links:

    print("DOWNLOADING--", end='')

    with requests.get(url, stream=True, cookies=cj) as r:
        try:
            fn = r.headers['content-disposition']
            text = re.findall('filename=(.+);', fn)[0]
            map_name = text.split('"')[1]

            for sign in notlist:
                if sign in map_name:
                    map_name = map_name.replace(sign, '_')

            # DON'T FORGET TO CHANGE THIS FOLDER
            fname = "D:\\frixacoder\\progs\\osu!\\Songs\\" + map_name
            print(r"{}".format(fname), end='')

            with open(fname, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            
            print("--DOWNLOADED")

        except:
            print("--Something went wrong!")
            
            # DON'T FORGET TO CHANGE THIS FOLDER
            with open("osumapdler\\errors.txt", 'a') as er:
                er.write(url)
                time.sleep(1)
        
