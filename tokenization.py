from collections import defaultdict, namedtuple
from chatbot import preprocessing


def mostFreqPair(pairCharFreq):
  return max(pairCharFreq.keys(), key=pairCharFreq.get)


def updateWordDict(word_dict, pairCharFreq, tl, tr, unique_letters):
  t_new = tl + tr 
  new_word_dict = defaultdict(int)
  unique_letters.add(t_new)
  for word in word_dict:
    new_word = word.replace(tl + tr, t_new)
    new_word_dict[new_word] = word_dict[word]
  print(new_word_dict)
  pairCharFreq.clear()
  for word, freq in new_word_dict.items():
    word_arr = list(word)
    for i in range(len(word_arr) - 1):
      pairChar = (word_arr[i], word_arr[i + 1])
      pairCharFreq[pairChar] = freq
  print(pairCharFreq)
  return new_word_dict, pairCharFreq

def bpe(sentence, k):
  sentence = preprocessing(sentence)
  unique_letters = (set(sentence.lower()))
  word_dict = defaultdict(int)
  for word in sentence.split():
    word_dict[word] += 1 
  
  pairCharFreq = defaultdict(int)
  for word in word_dict:
    word_arr = list(word)
    for i in range(len(word_arr) - 1):
      pairChar = (word_arr[i], word_arr[i + 1])
      pairCharFreq[pairChar] += word_dict[word]
  for _ in range (k):
    tl,tr = mostFreqPair(pairCharFreq)
    word_dict, pairCharFreq = updateWordDict(word_dict, pairCharFreq, tl, tr, unique_letters)
  return word_dict, sorted(unique_letters)
	
dict, vocab = bpe("HI HI HI , MY Name came inside same same, HI HI HI HI", 10)
print(vocab)