def bpe(sentence):
	sentence = sentence.lower()
	list_sentence = list(set(*[sentence]))
	return list_sentence

print (bpe("Hi! My name is the Shy"))