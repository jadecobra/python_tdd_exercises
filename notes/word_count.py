import string
import operator
import os
import json

def get_words(line):
    return (
        line.lower()
            .strip()
            .translate(
                line.maketrans("", "", string.punctuation)
            ).split()
    )

def get_lines(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except IsADirectoryError:
        return ()

def update_word_count(result=None, words=None):
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

def get_word_occurrences():
    result = dict()

    for filename in os.listdir():
        for line in get_lines(filename):
            result = update_word_count(result=result, words=get_words(line))
    return result

def to_json(dictionary, filename):
    print(f'writing word count to {filename}...')
    dictionary = dict(reversed(sorted(dictionary.items(), key=operator.itemgetter(1))))
    with open(filename, 'w') as file:
        json.dump(dictionary, file, indent=2)

if __name__ == '__main__':
    word_count = get_word_occurrences()
    to_json(word_count, 'notes/word_count.json')
    print('total word count: ', sum(word_count.values()))
    for name in sorted((
        'AssertionError',
        'AttributeError',
        'ModuleNotFoundError',
        'TypeError',
        'SyntaxError',
        'NameError',
        'KeyError',
        'IndexError',
    )):
        print(name, word_count.get(name.lower(), 0))
