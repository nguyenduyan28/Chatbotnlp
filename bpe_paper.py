import re, collections
from chatbot import preprocessing
def makeVocab(sentence):
  sentence = preprocessing(sentence) # remove punct and lower
  unique_letter = set(sentence)
  print(f'unique_letter is : {unique_letter}')
  for word in sentence.split():
    word = ' '.join(word)
    word += ' </w>'
    vocab[word] += 1
  return vocab, unique_letter


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

vocab, unique_letter = makeVocab("Hello, how are you doing?")
num_merges = 5

for _ in range(num_merges):
  pairs = get_stats(vocab)
  best = max(pairs, key=pairs.get)
  for arg in best:
    unique_letter.add(best)
  vocab = merge_vocab(best, vocab)



print(vocab)
print(sorted(unique_letter))
