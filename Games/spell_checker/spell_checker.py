from sklearn.datasets import fetch_20newsgroups
# text processing
import nltk
import operator
from nltk.corpus import stopwords
import re
from Trie import Trie
rep_numbers=re.compile(r'\d+',re.IGNORECASE)
rep_special_chars= re.compile("[^\w']|_")

data_train = fetch_20newsgroups(subset='train',remove = ('headers', 'footers', 'quotes'))
corpus_list = data_train.data


class Spell_Checker():
    def __init__(self, corpus_list):
        self.word_trie = Trie()
        for sentense in corpus_list:
            valid_words = self.text_to_words(sentense)
            for valid_word in valid_words:
                self.word_trie.add(valid_word)

    def text_to_words(self, text):
        text=rep_special_chars.sub(' ', text)
        text = rep_numbers.sub('', text) # get rid of numbers
        words = text.split() # Split string into words
        return words

    def check(self, sentence):
        words = self.text_to_words(sentence)
        list_to_check = []
        for w in words:
            if not self.word_trie.exists(w):
                list_to_check.append(w)

        if list_to_check:
            print('Check the spelling of the following words:')
            for w in  list_to_check:
                print(w)
        else:
            print('No spelling errors found')

    def read_check(self):
        request = input('Would you like to check a sentense: (y/n)')
        while request == 'y':
            input_sentense = input('Introduce the sentense you would like to check:')
            self.check(input_sentense)
            request = input('Would you like to check a sentense: (y/n)')


if __name__ == '__main__':
    spell_checker = Spell_Checker(corpus_list)
    spell_checker.read_check()
