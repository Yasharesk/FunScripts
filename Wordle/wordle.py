# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:32:34 2022

@author: Yashar
"""

from collections import Counter


def letter_count(word_list: list[str]) -> Counter:
    '''Count the number of occurances of every letter in the list'''
    cnt = Counter()
    for word in word_list:
        for letter in word:
            cnt[letter] += 1
    return cnt


def read_words() -> list[str]:
    '''Read the words from the file and create a list of 5 letter words'''
    words = []
    with open('Data/words') as f:
        for line in f.readlines():
            words.append(line.strip().lower())
    wordle_words = [x for x in words if len(x) == 5]
    wordle_words = [x for x in wordle_words if '\'' not in x]
    return wordle_words


def letter_missed(word_list: list[str], letter: str) -> list[str]:
    '''Update the word list if the letter is not in the word [response == 'm']'''
    return [x for x in word_list if letter not in x]


def letter_found(word_list: list[str], letter: str, i: int) -> list[str]:
    '''Update the word list if the letter is in the word not in the right place [response == 'y']'''
    w = [x for x in word_list if letter in x]
    w = [x for x in w if letter != x[i]]
    return w


def letter_hit(word_list: list[str], letter: str, i: int) -> list[str]:
    '''Update the word list if the letter is in the word in the right place [response == 'g']'''
    return [x for x in word_list if x[i] == letter]


def sort_by_score(word_list: list[str]) -> list[str]:
    '''
    Scores are calculated as the sum of the count of each letter in the list.
    List sorted by highest scores is returned.
    '''
    cnt = letter_count(word_list)
    word_list.sort(key=lambda x: sum([cnt[s] for s in x]), reverse=True)
    return word_list


def set_result(used: str, response: str) -> list[dict]:
    '''Transform the 'word used' and 'response' provided by the user to a code readable format'''
    result = list(enumerate(zip(used, response)))
    result = [{'index': x[0], 'letter': x[1][0], 'response': x[1][1]} for x in result] 
    return result


def main():
    wordle_words = read_words()
    print('Here are the first suggestions to start the game:')
    
    # For the first batch we remove words with duplicate letters to increase the number of hits/misses
    print(sort_by_score([x for x in wordle_words if len(set(x))==5])[:10])
    
    turns = 1
    while turns < 6:
        used = input('Word played: ')
        turns += 1
        chk = True
        while chk:
            response = input('Response: ')
            if (len(response) != 5) | (not (set(response).issubset(set('gmy')))):
                print('Check the response!')
            else:
                chk = False
        
        if response == 'ggggg':
            print('Nice!')
            input('')
            break
        result = set_result(used, response)
        for item in result:
            if item['response'] == 'm':
                wordle_words = letter_missed(wordle_words, item['letter'])
            elif item['response'] == 'g':
                wordle_words = letter_hit(wordle_words, item['letter'], item['index'])
            elif item['response'] == 'y':
                wordle_words = letter_found(wordle_words, item['letter'], item['index'])
        print(sort_by_score(wordle_words)[:10])
    if turns > 6:
        print('Damn it!')
        input('')


if __name__ == '__main__':
    main()
