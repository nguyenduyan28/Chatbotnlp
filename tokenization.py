from collections import defaultdict
from chatbot import preprocessing
def bpe(sentence):
  sentence = preprocessing(sentence)
  unique_letters = sorted(set(sentence.lower()))
  word_dict = defaultdict(int)
  for word in sentence.split():
    word_dict[word] += 1 
  for w in word_dict:
    print(w)
  print(unique_letters)
	
print(bpe("Hi! My name is the Shy"))