def bpe(sentence):
	return sorted(set(sentence.lower())) # it will return a list

print (bpe("Hi! My name is the Shy"))