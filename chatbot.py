import string



def checkNone(list):
	for char in list:
		if (char == ''): return False
		else: return True
def preprocessing(user_input):
	user_input = user_input.lower()
	# remove punctuation	
	non_punct = ''.join(list(map(lambda s: ' ' if s in string.punctuation else s , user_input))).split(' ')
	non_punct = ' '.join(list(filter(checkNone, non_punct)))
	return non_punct



def main():
	message = str(input("Take input something to say with chatbot: "))
	message = preprocessing(message)
	print(f"String with out punctuation:  {message}")

if __name__ == '__main__':
	main()
