import unittest
import csv
import re


class TestMethods(unittest.TestCase):  # Class containing all the tests that will be run
 def test_not_blank_answer(self) -> "Test getting the users name as not blank and not containing numbers":
  not_wanted = ''
  self.assertNotEqual((testing_function := get_user_name()), not_wanted, 'A blank output was returned')

 def test_get_user_age(self) -> "Test getting the users age as a valid age":
  not_wanted = ''
  self.assertNotEqual((testing_function := get_user_age()), not_wanted, 'A blank output was returned')

 def test_validate_number_valid(self) -> "Test validate_number for a valid input with noise":
  expected_outputs = True
  test_input = '9a%@*&^j;\'6.'
  self.assertEqual((testing_function := validate_age(test_input)), expected, 'Expected 96')

 def test_validate_number_invalid(self) -> "Test validate_number for an invalid input":
  expect_invalid = False
  test_invalid = 'Hello there!'
  self.assertEqual((testing_function := validate_age(test_invalid)), expect_invalid,
                   'Did not get Number invalid, expected Number invalid')

 def test_seat_available_low_and_high(self) -> "Test seat_available for not available and available situations":
  variables = [0, 101, 150]
  expected_outputs = [False, True, True]
  for index in range(len(expected_outputs)):
   self.assertEqual((testing_function := seat_available(150, variables[index])), expected_outputs[index],
                    'Did not get correct ouput: {}, instead got {}: Bug in seat_available'.format(
                     expected_outputs[index], seat_available(150, variables[index])))


def seat_available(max_available=150, available_seats=0) -> "Return True if there is a seat available":
 if max_available >= available_seats > 0:
  return True
 return False


def get_user_name() -> "Return the persons name":
 return ask_question('What is your first name?', '[a-zA-Z]')


def get_user_age(min_age=12, max_age=130) -> "Return the persons age":
 if validate_age(response := ask_question('What is your age?', '[0-9]'), min_age, max_age):
  return response
 print("Your age must be an integer between {} and {}".format(min_age, max_age))
 return get_user_age(min_age, max_age)


def ask_question(ask='', valid_characters='') -> "Ask question until the answer is not blank":
 if (answer := (''.join(re.findall(valid_characters, input(ask))))) != '':
  return answer
 print('Input cannot be blank {}'.format(answer))
 return ask_question(ask, valid_characters)


def validate_age(number='', low_range=12, high_range=130) -> "Validate if the users age is valid":
 # add 0 so no blank and divide by 10 to remove shifting
 if high_range > (answer := int((''.join(re.findall('[0-9]', number)) + '0')) // 10) > low_range:
  return True
 return False


if __name__ == '__main__':
 unittest.load_tests(TestMethods)
 unittest.main()
