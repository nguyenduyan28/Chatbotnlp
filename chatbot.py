import string




def preprocessing(user_input):
	user_input = user_input.lower()
	# remove punctuation	
	punct_set = set()
	for char in user_input:
		if (char in string.punctuation):
			punct_set.add(char)
		print(char for char in user_input if char in string.punctuation)		
	# punct_set.add(char for char in user_input if char in string.punctuation)
		# print(punct_set)
		user_input = user_input.replace(str(punct for punct in punct_set), '')
		
	return user_input


def main():
	message = str(input("Take input something to say with chatbot: "))
	message = preprocessing(message)
	print(f"String with out punctuation {message}")

if __name__ == '__main__':
	main()
