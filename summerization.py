# -*- coding: utf-8 -*-
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.web_scraping import WebScraping
# from pysummarization.abstractabledoc.std_abstractor import StdAbstractor
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


def Main(file):
    with open(file,encoding="utf-8") as f:
      document = f.read()

    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer. This is japanese tokenizer with MeCab.
    auto_abstractor.tokenizable_doc = MeCabTokenizer()
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(document, abstractable_doc)
    
    # Output 3 summarized sentences.
    limit = 3
    i = 1
    for sentence in result_dict["summarize_result"]:
        print(sentence)
        if i >= limit:
            break
        i += 1

if __name__ == "__main__":
    Main('text/text.txt')# -*- coding: utf-8 -*-
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.web_scraping import WebScraping
# from pysummarization.abstractabledoc.std_abstractor import StdAbstractor
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


def Main():
    '''
    Entry point.
    
    Args:
        url:    target url.
    '''
    # Object of web scraping.
    web_scrape = WebScraping()
    # Web-scraping.
    with open('text/text.txt',encoding="utf-8") as f:
      document = f.read()

    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer. This is japanese tokenizer with MeCab.
    auto_abstractor.tokenizable_doc = MeCabTokenizer()
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(document, abstractable_doc)
    
    # Output 3 summarized sentences.
    limit = 3
    i = 1
    for sentence in result_dict["summarize_result"]:
        print(sentence)
        if i >= limit:
            break
        i += 1

if __name__ == "__main__":
    Main()