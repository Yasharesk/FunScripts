from wordle_classbased import Wordle


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
        print(f'{used} was played and the response was {response}')
        if response == 'ggggg':
            print(f'Win in {cnt} moves on the word {test_word}')
            break
        wordle.play_round(used, response)
        if len(wordle.wordle_words) == 0:
            print(f'The word {test_word} was not found')
    if wordle.turn > 6:
        print(f'Failed with a list of {len(wordle.wordle_words)} remaining')


test_words = ['liver', 'llama', 'apple']
for test_word in test_words:
    print('-------------------------------------------')
    test_play(test_word)