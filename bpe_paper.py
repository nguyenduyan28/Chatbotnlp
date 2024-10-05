import re, collections
from chatbot import preprocessing

def makeVocab(sentence):
  sentence = preprocessing(sentence) # remove punct and lower
  vocab = collections.defaultdict(int)

  for word in sentence.split():
    word = ' '.join(word)
    word += ' </w>'
    vocab[word] += 1
  return vocab


def get_stats(vocab):
  pairs = collections.defaultdict(int)
  for words, freq in vocab.items():
    char = words.split()
    for i in range(len(char) - 1):
      pairs[char[i], char[i + 1]] += freq
  return pairs
    
# not clear 
def merge_vocab(pair, v_in):
  v_out = {}
  bigram = re.escape(' '.join(pair))
  p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
  for word in v_in:
    new_word = p.sub(''.join(pair), word)
    v_out[new_word] = v_in[word]
  return v_out

#vocab = {'l o w </w>' : 5, 'l o w e r </w>' : 2}

vocab = makeVocab("Hi djfalkfjalkfj ngu ngu!!!,m !!!")
num_merges = 10
for _ in range(num_merges):
  pairs = get_stats(vocab)
  best = max(pairs, key=pairs.get)
  vocab = merge_vocab(best, vocab)
  print(vocab)
  print(best)
  



