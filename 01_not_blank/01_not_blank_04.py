import unittest


class TestMethods(unittest.TestCase):
	def test_not_blank_answer(self):
		expected = ''
		self.assertNotEqual((testing_function := not_blank('What is your name?')), expected, 'A blank output was returned')


def not_blank(ask='') -> "Ask question until the answer is not blank":
	if (answer := input(ask)) != '' or print('Input cannot be blank') or (answer := not_blank(ask)) != '': return answer


# name = not_blank('What is your name?: '); print('Hello {}'.format(name))

if __name__ == '__main__':
	unittest.load_tests(TestMethods)
	unittest.main()
