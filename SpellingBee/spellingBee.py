from os import path

WORDS_FILE = 'words'
WORDS_DIR = ''

# test_list = 'etcapyf'
# test_center = 'f'
# letters = test_list
# center = test_center

with open(path.join(path.dirname(__file__), WORDS_DIR, WORDS_FILE)) as f:
    word_list = f.readlines()

word_list = [w.strip('\n').lower() for w in word_list]
word_list = [w for w in word_list if len(w)>3]
word_list = [w for w in word_list if "'" not in w]

def check(word: set[str], letters: set[str], center: str):  
    if center not in word:
        return False
    elif not word.issubset(letters):
        return False
    else:
        return True

letters = input('List of letters: ').strip().lower()
center = input('Center letter: ').strip().lower()

result = [w for w in word_list if check(set(w), set(letters), center)]
print(result)