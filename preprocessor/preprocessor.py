from string import ascii_letters
import re
import time


class Preprocessor:

    ngram_step = 2
    symbolic_ngram_step = 3

    def __init__(self, text, use_part_of_text=None):

        if use_part_of_text:
            # TODO: split text to percents of usage
            pass

        self.raw_text = text
        self.words = []
        self.ngram = []
        self.symbolic_ngram = []

    def tokenize(self, tokenize_date=False, tokenize_currency=False, filter_tags=True):
        assert type(self.raw_text) == str
        text = self.raw_text
        text = text.strip().lower()

        if tokenize_date:
            # TODO: all dates to special symbol (regex)
            pass

        if tokenize_currency:
            # TODO: all currency to special symbol (regex)
            pass

        if filter_tags:
            text = ' '.join([word for word in text.split() if not word.startswith('#')])


        # Remove punctuation
        # TODO: optimize
        text = ''.join(ch for ch in text if ch in ascii_letters + ' ')

        self.words = text.split()
        self.ngram = [[self.words[i + j] for j in range(self.ngram_step)] for i in
                      range(len(self.words) - self.ngram_step + 1)]

        text = text.replace(' ', '*')
        self.symbolic_ngram = [[text[i + j] for j in range(self.symbolic_ngram_step)] for i in
                      range(len(text) - self.symbolic_ngram_step + 1)]

        a = 0

if __name__ == '__main__':
    file_path = '/home/stas/Projects/stas/ml-ucu-2/winter-ml-nlp/cnn-classifier/prima/ctgrs'
    file_name = 'alcohol.txt'
    file_path += '/' + file_name

    with open(file_path, 'r') as f:
        text = f.read()

    p = Preprocessor(text)
    p.tokenize()

