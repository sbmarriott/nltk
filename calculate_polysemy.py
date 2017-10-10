'''
From wordnet.princeton.edu:
WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept. 
Synsets are interlinked by means of conceptual-semantic and lexical relations. The resulting network of meaningfully related words and concepts can be navigated with the browser. 
WordNet is also freely and publicly available for download. 
WordNet's structure makes it a useful tool for computational linguistics and natural language processing.
'''
# Using WordNet, compute the average polysemy of nouns, verbs, adjectives and adverbs 
nouns = list(wn.all_synsets(wn.NOUN))
adjectives = list(wn.all_synsets(wn.ADJ))
verbs = list(wn.all_synsets(wn.VERB))
adverbs = list(wn.all_synsets(wn.ADJ))
def calculatewords(synset):
	words = []
	for syn in synset:
		words += syn.lemma_names()
	total = len(set(words))
	return total
def calculatesenses(synset):
	senses = sum(1 for x in synset)
	return senses
def calculateaverage(synset):
	average = calculatesenses(synset) / calculatewords(synset)
	return average
print('Nouns: ', calculateaverage(nouns))
print('Adjectives: ', calculateaverage(adjectives))
print('Verbs: ', calculateaverage(verbs))
print('Adverbs: ', calculateaverage(adverbs))
