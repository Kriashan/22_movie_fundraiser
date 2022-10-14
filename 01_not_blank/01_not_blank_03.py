#1672015255.266918
def not_blank(question='') -> "Ask question until the answer is not blank":
	while (answer := input(question)) == '':
		print("That name is blank!")
	return answer


print("Hello {}".format(not_blank('What is your name?: ')))
