def get_question(question=input("What is your question?"))
	while question != "quit":
		if question[-1] == “?”:
			return question
		else:
			print(“Sorry, I can only answer questions”)