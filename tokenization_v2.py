from collections import namedtuple, defaultdict
from chatbot import preprocessing




def bpe(sentence, k):
  sentence = preprocessing(sentence)
  vocab = set(sentence)
  freqWord = defaultdict(int)
  Corpus = namedtuple('Corpus', ['word', 'freq'])
  list_corpus = []
  for word in sentence.split():
    freqWord[word] += 1
    corpus = Corpus(word, (freqWord[word]))
    list_corpus.append(corpus)
  print(list_corpus)




bpe("HI HI HI , MY Name came inside same same, HI HI HI HI", 10)