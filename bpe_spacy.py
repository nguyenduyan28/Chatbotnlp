import spacy


chatbot = spacy.load('en_core_web_sm')
s = 'Hello, how are you doing?'


doc = chatbot(s)
print([word.text for word in doc])