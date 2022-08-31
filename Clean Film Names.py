# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 01:14:05 2020

@author: Yashar
"""

import os
import re
from tkinter import filedialog


REMOVE_LIST = r'720p|BluRay|x264|YIFY|juggs|\[ETRG\]|HDRip|\[YTS.AG\]|dvdrip|xvid|ETRG|HDTV|\
        |H264|AC3|xvid|aac|brrip|\[|\]|\{|\}|saas|mp3|rarbg|web-dl|1080p|dvdscr|tehmovies|\
            teh-music|mkvcage| Hc|ganool|-Evo|bdrip|teh-music|nex1movie|shaanig|\
        Korsub|webrip|aqos|S4A|-sam|blu-ray| biz|480p|Mkvhub|Film2Movie|Galaxyrg|\
            Tehtmovies|- Com|Iran-film|30Nama|Wb-Dl|x265|2Ch|10Bit|Psa|Pahe'
INITIAL_DIR = 'D:/Downloads/'


def remove_extra_words(file_name: str, remove_list: str = REMOVE_LIST) -> str:
    file_name = re.sub(remove_list, '', file_name, flags=re.IGNORECASE)
    file_name = re.sub('\.', ' ', file_name, flags=re.IGNORECASE)
    file_name = re.sub('_', ' ', file_name, flags=re.IGNORECASE)
    file_name = re.sub('  ', ' ', file_name, flags=re.IGNORECASE)
    file_name = file_name.strip().title()
    file_name = file_name.strip('-')
    file_name = re.sub('file', 'changed', file_name, flags=re.IGNORECASE)
    return file_name.strip().title()


def clean_directory(folder_path: str) -> None:
    mypath = list(reversed(list(os.walk(folder_path))))
    for item in mypath:
        for file_name in item[2]:
            f_name, f_ext = os.path.splitext(file_name)
            os.rename(os.path.join(item[0], file_name), os.path.join(item[0], remove_extra_words(f_name)+f_ext))
        if len(item[1])>0:
            for dir_name in item[1]:
                os.rename(os.path.join(item[0], dir_name), os.path.join(item[0], remove_extra_words(dir_name)))


def main() -> None:
    folder_path = filedialog.askdirectory(title='Select directory', initialdir=INITIAL_DIR)
    if len(folder_path) > 0:
        clean_directory(folder_path)


if __name__ == '__main__':
    main()