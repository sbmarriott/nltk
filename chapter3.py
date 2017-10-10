# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:35:46 2017

@author: Sarah Beth Marriott
"""

import nltk
from nltk.book import *
from nltk.corpus import wordnet as wn
# 3.1 ☼ Define a string s = 'colorless'. Write a Python statement that changes this to "colourless" using only the slice and concatenation operations.
s = 'colorless'
s = s[:4] + 'u' + s[4:]
print(s)
# 3.3 ☼ We saw how we can generate an IndexError by indexing beyond the end of a string. Is it possible to construct an index that goes too far to the left, before the start of the string?
string = "test"
''' string[-5] '''
string[-5:4]
print("The first index (commented out to avoid error when running program) results in an IndexError, but the second does not. Therefore, it is possible to go too far to the left if you index a string, but it will not produce an error when you use slicing.")
# 3.4 ☼ We can specify a "step" size for the slice. The following returns every second character within the slice:  monty[6:11:2]. It also works in the reverse direction: monty[10:5:-2] Try these for yourself, then experiment with different step values.
monty = "Monty Python"
monty[6:11:2]
monty[10:5:-2]
monty[0:11:2]
monty[11:0:-2]
monty[2:5:3]
# 3.5 ☼ What happens if you ask the interpreter to evaluate monty[::-1]? Explain why this is a reasonable result.
monty[::-1]
print("This reverses the string. The 'step' size is -1 and the start and ending points of the slice are not specified, so they are run at the default of 1.")
# 3.10 ☼ Rewrite the following loop as a list comprehension:
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = [(word, len(word)) for word in sent]
result
# 2.14 ◑ Define a function supergloss(s) that takes a synset s as its argument and returns a string consisting of the concatenation of the definition of s, and the definitions of all the hypernyms and hyponyms of s.
def supergloss(s):
    word = wn.synset(s)
    definition = word.definition()
    hypdefinitions = [w.definition() for w in word.hypernyms()]
    hypodefinitions = [w.definition() for w in word.hyponyms()]
    return ('Original: ', word), ('Hypernyms: ', ". ".join(hypdefinitions)), ('Hyponyms: ', ". ".join(hypodefinitions))
# 2.17 ◑ Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.
stopwords = nltk.corpus.stopwords.words('english')
def ex17(text):
    fdist = nltk.FreqDist([w for w in text.words() if w.isalpha() and w not in stopwords])
    words = [sample for sample, outcome in fdist.most_common(50)]
    return words
ex17(nltk.corpus.brown)
# 2.18 ◑ Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.
def ex18(text):
    fdist = nltk.FreqDist([w for w in nltk.bigrams(text.words()) if w[0] not in stopwords and w[1] not in stopwords and w[0].isalpha() and w[1].isalpha()])
    bigrams = [sample for sample, outcome in fdist.most_common(50)]
    return bigrams
ex18(nltk.corpus.brown)
# 2.22 ◑ Define a function hedge(text) which processes a text and produces a new version with the word 'like' between every third word.
def hedge(text):
    like_text = []
    word = 0
    for w in text:
        like_text.append(w)
        word = word + 1
        if word % 3 == 0:
            like_text.append('like')
    return like_text
hedge(text3)
