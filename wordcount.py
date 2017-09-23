import string
def print_words():
    f = open('text.txt', 'r', encoding='utf-8')
    punctuation_symbols = string.punctuation + string.whitespace
    text = f.read().lower().split()
    dict = {}
    for word in text:
        word = word.strip(punctuation_symbols)
        if len(word) > 1 and word.isalpha():
            dict[word] = dict.get(word,0) + 1
    return dict


def print_top_words():
    words = print_words()
    for k, v in sorted(words):
        print('{:20} {:5}'.format(k,v))




print_top_words()