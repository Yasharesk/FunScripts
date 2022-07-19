from wordle_classbased import Wordle
from datetime import datetime

def check_guess(word: str, guess: str) -> str:
    result = ''
    for i, s in enumerate(guess):
        if s == word[i]:
            result += 'g'
        elif s in word:
            result += 'y'
        else:
            result += 'm'
    return result


def test_play(test_word: str):
    wordle = Wordle()
    cnt = 0
    while wordle.turn <= 6:
        cnt += 1
        used = wordle.wordle_words[0]
        response = check_guess(test_word, used)
        # print(f'{used} was played and the response was {response}')
        if response == 'ggggg':
            return {'result': 'WIN', 'moves': cnt, 'test_word': test_word}
        wordle.play_round(used, response)
        if len(wordle.wordle_words) == 0:
            return {'result': 'NOT_FOUND', 'moves': cnt, 'test_word': test_word}
            
    if wordle.turn > 6:
        return {'result': 'OUT_OF_MOVES', 'moves': cnt, 'test_word': test_word, 'remaining': len(wordle.wordle_words)}


test_words = ['liver', 'llama', 'apple', 'wedge']
for test_word in test_words:
    print('-------------------------------------------')
    result = test_play(test_word)
    match result.get('result'):
        case 'WIN':
            print(f'Win in {result.get("moves")} moves on the word {result.get("test_word")}')
        case 'NOT_FOUND':
            print(f'The word {result.get("test_word")} was not found')
        case 'OUT_OF_MOVES':
            print(f'Failed with a list of {result.get("remaining")} remaining')


w = Wordle()
total_words = len(w.wordle_words)
wins = 0
loses = []
for test_word in w.wordle_words:
    result = test_play(test_word)
    if result.get('result') == 'WIN':
        wins += 1
    else:
        loses.append(result)

print(f'Win rate was {wins/total_words*100:.2f} and loses on {len(loses)} words')
with open(f'Data/losing_words_{datetime.today().strftime("%y-%m-%d")}.txt', 'w') as f:
    f.writelines([f'{item.get("result")}: {item.get("test_word")}' for item in loses])

