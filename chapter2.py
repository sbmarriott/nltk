# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:13:37 2017

@author: Sarah Beth Marriott
"""
import nltk, random
from nltk import FreqDist
from nltk.corpus import gutenberg, state_union, brown

# Question 2: Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?
austen = gutenberg.words('austen-persuasion.txt')
print('This book has ', len(austen), 'word tokens and ', len(set(austen)), 'word types.')
len(set(austen))

# Question 3: Use the Brown corpus reader nltk.corpus.brown.words() or the Web text corpus reader  nltk.corpus.webtext.words() to access some sample text in two different genres.
nltk.corpus.brown.words(categories=['news'])
nltk.corpus.brown.words(categories=['mystery'])

# Question 4: Read in the texts of the State of the Union addresses, using the state_union corpus reader. Count occurrences of men, women, and people in each document. What has happened to the usage of these words over time?
nltk.corpus.state_union.fileids()
nltk.corpus.state_union.words()
cfd = nltk.ConditionalFreqDist(
        (word, id[:4])
        for id in state_union.fileids()
        for y in state_union.words(id)
        for word in ["men", "women", "people"]
      if y.lower() == word)
cfd.plot()
print("It appears that for the most part the use of men, women, and people has been fairly steady. However, over time there have been several notable peaks, especially in the use of 'people.' The largest peak occured in the mid to late 1990s.")

''' Question 7: According to Strunk and White's Elements of Style, the word however, used at the start of a sentence, means "in whatever way" or "to whatever extent", and not "nevertheless". They give this example of correct usage: 
    However you advise him, he will probably do as he thinks best. (http://www.bartleby.com/141/strunk3.html) Use the concordance tool to study actual usage of this word in the various texts we have been considering. 
    See also the LanguageLog posting "Fossilized prejudices about 'however'" at  http://itre.cis.upenn.edu/~myl/languagelog/archives/001913.html
'''
gutenberg.fileids()
mobydick = nltk.Text(nltk.corpus.gutenberg.words('melville-moby_dick.txt'))
austen = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
mobydick.concordance('however')
austen.concordance('however')
print("In the Moby Dick text, where the word 'however' was used at the beginning of a sentence, it seemed to have the meaning of 'nevertheless,' so this would contradict Strunk and White's hypothesis. There was one instance that complied with the hypothesis in Moby Dick: 'However contracted, that definition is the...'. In the Austen-Emma text, I found the same results. I would argue that the presence of a comma immediately after the word 'however' often correlates to it holding the meaning of 'nevertheless' instead of 'to whatever extent.")

# Question 8: Define a conditional frequency distribution over the Names corpus that allows you to see which initial letters are more frequent for males vs. females (cf. 4.4).
names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')
cfd = nltk.ConditionalFreqDist(
        (fileid, name[0])
        for fileid in names.fileids()
        for name in names.words(fileid))
cfd.plot()
    
# Question 12: The CMU Pronouncing Dictionary contains multiple pronunciations for certain words. How many distinct words does it contain? What fraction of words in this dictionary have more than one possible pronunciation?
entries = nltk.corpus.cmudict.entries()
words = [word for word, pron in entries]
distinct = set(words)
fraction = 1-(len(distinct))/len(words)
print("There are ", len(distinct), "distinct words in the CMU Pronouncing Dictionary.", format(fraction, '.5f'), " of words in the dictionary have more than one possible pronunciation.")
