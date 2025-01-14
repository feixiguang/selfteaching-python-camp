#!/usr/bin/python

import string
import jieba
from collections import Counter

def stats_text_en(en_text):
    if not isinstance(en_text, str):
        raise ValueError("The method only accepts type str.")

    for en_special_word in string.punctuation:
        if en_special_word in en_text:
            en_text = en_text.replace(en_special_word, "")

    en_word_counter = Counter()
    en_text = en_text.split()
    for en_word in en_text:
        en_word_counter[en_word] += 1

    return en_word_counter.most_common()


def stats_text_cn(cn_text):
    if not isinstance(cn_text, str):
        raise ValueError("The method only accepts type str.")

    #cn_special_words = "！“”#$%&‘’（）*+，-。/：；、……<=>？@[]「」《》^_`{|}~\n"
    #for cn_special_word in cn_special_words:
    #    if cn_special_word in cn_text:
    #        cn_text = cn_text.replace(cn_special_word, "")
    
    #把字符串给cut作为第一个参数
    cn_text = jieba.cut(cn_text, cut_all=False)

    cn_word_counter = Counter()
    for cn_word in cn_text:
        cn_word_counter[cn_word] += 1

    return cn_word_counter.most_common()


def stats_text(en_text, cn_text):
    if (not isinstance(en_text, str)) or (not isinstance(cn_text, str)):
        raise ValueError("The method only accepts type str.")

    return stats_text_en(en_text), stats_text_cn(cn_text)
