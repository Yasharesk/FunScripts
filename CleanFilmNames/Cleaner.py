import os
import re


class DirCleaner:
    def __init__(self, dir_path: str,  remove_list: str) -> None:
        self.remove_list = '|'.join(remove_list.split(','))
        self.dir_path = dir_path


    def add_words(self, additional_words: str) -> None:
        additional_words = '|'.join(additional_words.split(','))
        additional_words = re.sub(r'[^\|\w\d]', '', additional_words)
        print(f'additional words: {additional_words}')
        self.remove_list += '|'
        self.remove_list += additional_words

    
    def clean_file_name(self, file_name: str) -> str:
        file_name = re.sub(r'[\._\s{2,}]', ' ', file_name, flags=re.IGNORECASE)
        file_name = re.sub(r'[\[\]]', ' ', file_name, flags=re.IGNORECASE)
        file_name = re.sub(self.remove_list, '', file_name, flags=re.IGNORECASE)
        file_name = file_name.strip().strip('-')
        return file_name.title()


    def clean_directory(self) -> None:
        mypath = list(reversed(list(os.walk(self.dir_path))))
        for item in mypath:
            for file_name in item[2]:
                f_name, f_ext = os.path.splitext(file_name)
                os.rename(os.path.join(item[0], file_name), os.path.join(item[0], self.clean_file_name(f_name)+f_ext))
            if len(item[1])>0:
                for dir_name in item[1]:
                    os.rename(os.path.join(item[0], dir_name), os.path.join(item[0], self.clean_file_name(dir_name)))
