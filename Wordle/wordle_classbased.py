# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:32:34 2022

@author: Yashar
"""
from collections import Counter


class Wordle():
    def __init__(self) -> None:
        self.turn = 1
        self.wordle_words = []
        with open('Data/words') as f:
            for line in f.readlines():
                self.wordle_words.append(line.strip().lower())
        self.wordle_words = [x for x in self.wordle_words if len(x) == 5]
        self.wordle_words = [x for x in self.wordle_words if '\'' not in x]
        # self.wordle_words = [x for x in self.wordle_words if len(set(x)) == 5]
        self.sort_by_score()


    def letter_response(self, letter: str, i: int, response: str) -> None:
        if response == 'm':
            self.wordle_words = [x for x in self.wordle_words if letter not in x]
        elif response == 'y':
            self.wordle_words = [x for x in self.wordle_words if letter in x]
            self.wordle_words = [x for x in self.wordle_words if letter != x[i]]
        elif response == 'g':
            self.wordle_words = [x for x in self.wordle_words if x[i] == letter]
        else:
            raise ValueError('Response letter not recognized')   


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
        for item in self.result:
            self.letter_response(item['letter'], item['index'], item['response'])
        self.sort_by_score()
        print(self.wordle_words[:10]) 
        self.turn += 1
        


def main():
    wordle = Wordle()
    print('Here are the first suggestions to start the game:')
    print(wordle.wordle_words[:10])
    
    while wordle.turn <= 6:
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
