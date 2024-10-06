from transformers import GPT2Tokenizer

# Load GPT-2 tokenizer (which uses BPE)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Tokenize a sentence
sentence = "Hello, how are you?"
encoded_sentence = tokenizer.tokenize(sentence)
print("BPE Tokenized Sentence:", encoded_sentence)

# Convert tokens to input IDs
input_ids = tokenizer.convert_tokens_to_ids(encoded_sentence)
print("Token IDs:", input_ids)

# Decode back to the original sentence
decoded_sentence = tokenizer.decode(input_ids)
print("Decoded Sentence:", decoded_sentence)
