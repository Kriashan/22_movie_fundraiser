def not_blank(question):
	while True:
		answer = input(question)
		if answer != '':
			break
		print("That name is blank!")
	return answer


name = not_blank('What is your name?: ')
print('Hello, {}'.format(name))
