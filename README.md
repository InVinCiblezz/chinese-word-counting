# Chinese-Word-Counting

Chinese-Word-Counting is a Python script to **count, filter** chinese words and **determine** PoS (part of speech) using [**Jieba**](https://github.com/fxsjy/jieba).


## Installation
The preferred version of Python is 3.7.

```
python3 -m pip install jieba
python3 -m pip install paddlepaddle-tiny==1.6.1
```
## Usage
Replace your article with the contents in **sample.txt**.
```
python3 chinese_word_count.py
```
Will generate two CSV files: **CWA.csv** and **CWAW.csv**.

**CWA.csv** is the word counting result after [**Jieba**](https://github.com/fxsjy/jieba).

**CWAW.csv** is the result of **CWA.csv** filtered by **wordList.txt** (you can insert or remove words any time).