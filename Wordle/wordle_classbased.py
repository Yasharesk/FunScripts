# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:32:34 2022

@author: Yashar
"""
from collections import Counter
from typing import List
from os import path

WORDS_FILE = 'words'
WORDS_PATH = 'Data'


def create_word_list():
    wordle_words = []
    with open(path.join(WORDS_PATH, WORDS_FILE)) as f:
        for line in f.readlines():
            wordle_words.append(line.strip().lower())
    wordle_words = [x for x in wordle_words if len(x) == 5]
    wordle_words = [x for x in wordle_words if '\'' not in x]
    return wordle_words

class Wordle():
    def __init__(self, wordle_words: List[str]) -> None:
        self.turn = 1        
        self.wordle_words = wordle_words
        self.sort_by_score()


    def letter_response(self) -> None:
        greens = [x['letter'] for x in self.result if x['response'] == 'g']
        for item in self.result:
            match item['response']:
                case 'g': 
                    self.wordle_words = [x for x in self.wordle_words if x[item['index']] == item['letter']]
                case 'y': 
                    self.wordle_words = [x for x in self.wordle_words if item['letter'] in x]
                    self.wordle_words = [x for x in self.wordle_words if item['letter'] != x[item['index']]]
                case 'm':
                    if item['letter'] not in greens:
                        self.wordle_words = [x for x in self.wordle_words if item['letter'] not in x]
                case _:
                    raise ValueError('Response letter not recognized')
            
            
            ''' For Python version < 10'''
            # if item['response'] == 'g':
            #     self.wordle_words = [x for x in self.wordle_words if x[item['index']] == item['letter']]
            # elif item['response'] == 'y':
            #     self.wordle_words = [x for x in self.wordle_words if item['letter'] in x]
            #     self.wordle_words = [x for x in self.wordle_words if item['letter'] != x[item['index']]]
            # elif item['response'] == 'm':
            #     if item['letter'] not in greens:
            #         self.wordle_words = [x for x in self.wordle_words if item['letter'] not in x]
            # else:
            #     raise ValueError('Response letter not recognized')


    def sort_by_score(self) -> None:
        '''
        Scores are calculated as the sum of the count of each letter in the list.
        List sorted by highest scores is returned.
        '''
        cnt = Counter()
        for word in self.wordle_words:
            for letter in set(word):
                cnt[letter] += 1
        self.wordle_words.sort(key=lambda x: sum([cnt[s] for s in set(x)]), reverse=True)


    def set_result(self, used: str, response: str) -> None:
        '''Transform the 'word used' and 'response' provided by the user to a code readable format'''
        self.result = list(enumerate(zip(used, response)))
        self.result = [{'index': x[0], 'letter': x[1][0], 'response': x[1][1]} for x in self.result] 


    def play_round(self, used: str, response: str) -> None:
        self.set_result(used, response)
        self.letter_response()
        self.sort_by_score()
        self.turn += 1
        


def main():
    wordle = Wordle(create_word_list())
    print('Here are the first suggestions to start the game:')
    
    while wordle.turn <= 6:
        print(wordle.wordle_words[:10])
        used = input(f'Word played No. {wordle.turn}: ')
        chk = True
        while chk:
            response = input('Response: ')
            if (len(response) != 5) | (not (set(response).issubset(set('gmy')))):
                print('Check the response!')
            else:
                chk = False
        if response == 'ggggg':
            input('Nice!')
            break
        wordle.play_round(used, response)
    if wordle.turn > 6:
        input('Damn it!')


if __name__ == '__main__':
    main()
