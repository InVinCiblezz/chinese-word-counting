import jieba
import re
import csv
import jieba.posseg as pseg
from collections import Counter

# set values
sample = open("sample.txt", encoding="utf-8").read()
word_list = open("wordList.txt", encoding="utf-8").read()
word_PoS_dict = {"ns": "direction", "nw": "title",
                 "vd": "vadv", "a": "adj", "d": "adv",
                 "m": "nu", "q": "mw", "r": "pn",
                 "p": "prep", "c": "conj", "w": "punc",
                 "PER": "Name", "nr": "Name"}

find = word_list.split()
find = set(find)


def get_PoS(word):
    words = pseg.cut(word[0], use_paddle=True)
    PoS = 'qw'
    n = 0
    for w, f in words:
        n += 1
        PoS = word_PoS_dict[f] if f in word_PoS_dict else f
        if n > 1:
            PoS = 'qw'  # question word
    return PoS


def word_count_analysis(txt):
    seg_list = jieba.cut(txt, cut_all=False)
    counts = Counter(seg_list)
    CWA, CWAW = [], []
    jieba.enable_paddle()
    for word in counts.most_common():
        if re.search(u'[\u4e00-\u9fff]', word[0]):  # if chinese words
            PoS = get_PoS(word[0])
            CWA.append((word[0], PoS, word[1]))
            # word in wordList
            if word[0] in find:
                CWAW.append((word[0], PoS, word[1]))
    # write csv
    with open('CWA.csv', 'w', newline='') as csv_file:
        spamwriter = csv.writer(csv_file, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Word', 'PoS', 'Count'])
        for item in CWA:
            spamwriter.writerow(item)

    with open('CWAW.csv', 'w', newline='') as csv_file:
        spamwriter = csv.writer(csv_file, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Word', 'PoS', 'Count'])
        for item in CWAW:
            spamwriter.writerow(item)


word_count_analysis(sample)

