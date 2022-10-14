#1672015255.2719011
def not_blank(question):
	answer = input(question)
	while answer == '':
		print("That name is blank!")
		answer = input(question)
	return answer


name = not_blank('What is your name?: ')
print('Hello, {}'.format(name))
