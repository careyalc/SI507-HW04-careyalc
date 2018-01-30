import random

def get_question(question=input("What is your question?")):
	while question != "quit":
		if question[-1] == "?":
			return question
		else:
			print("Sorry, I can only answer questions")



def return_answer(q):
	list_of_possible_answers=["it is certain", "it is decidedly so", "without a doubt", "yes definitely", "you may rely on it", "as I see it, yes", "most likely", "outlook good", "yes", "signs point to yes", "reply hazy try again", "ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again", "don't count on it", "my reply is no", "my sources say no", "outlook not so good", "very doubtful"]
	print(random.choice(list_of_possible_answers))


return_answer(get_question())