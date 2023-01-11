# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# 原文
ORIGINAL = "text/en_text.txt"
# 要約分の保存先
SUMMARIZED = "text/results.txt"

# もともとの行数を取得
f = open(ORIGINAL, 'r', encoding='UTF-8') 
t = f.read()
f.close()
SENTENCE_NUM = t.count(".")

LANGUAGE = "english"
# 10%の行数になるように要約する
# 1行にまとめるのは少なすぎるから最低二行で
SENTENCES_COUNT = int(SENTENCE_NUM * 0.1)
if SENTENCES_COUNT < 2:
    SENTENCES_COUNT = 2

f = open(SUMMARIZED, 'w', encoding='UTF-8')
if __name__ == "__main__":

    parser = PlaintextParser.from_file(ORIGINAL, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

# 要約された文章を書き込む
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        text = str(sentence)
        f.write(text)
        f.write("\n")
    f.close()
print("finnished!")