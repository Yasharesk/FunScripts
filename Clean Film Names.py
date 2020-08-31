# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 01:14:05 2020

@author: Yashar
"""

import os
import re
os.chdir('I:/Movies/')

def clean(f):
    rem = r'720p|BluRay|x264|YIFY|juggs|\[ETRG\]|HDRip|\[YTS.AG\]|dvdrip|xvid|ETRG|HDTV|\
        |H264|AC3|xvid|aac|brrip|\[|\]|\{|\}|saas|mp3|rarbg|web-dl|1080p|dvdscr|tehmovies|\
            teh-music|mkvcage| Hc|ganool|-Evo|bdrip|teh-music|nex1movie|shaanig|\
        Korsub|webrip|aqos|S4A|-sam|blu-ray| biz|480p|Mkvhub|Film2Movie|Galaxyrg|\
            Tehtmovies|- Com|Iran-film|30Nama|Wb-Dl|x265'
    f = re.sub(rem, '', f, flags=re.IGNORECASE)
    f = re.sub('\.', ' ', f, flags=re.IGNORECASE)
    f = re.sub('_', ' ', f, flags=re.IGNORECASE)
    f = re.sub('  ', ' ', f, flags=re.IGNORECASE)
    f = f.strip().title()
    f = f.strip('-')
    f = re.sub('file', 'changed', f, flags=re.IGNORECASE)
    return f.strip().title()

mypath = list(reversed(list(os.walk('./'))))

for item in mypath:
    for file_name in item[2]:
        f_name, f_ext = os.path.splitext(file_name)
        os.rename(os.path.join(item[0], file_name), os.path.join(item[0], clean(f_name)+f_ext))
    if len(item[1])>0:
        for dir_name in item[1]:
            os.rename(os.path.join(item[0], dir_name), os.path.join(item[0], clean(dir_name)))