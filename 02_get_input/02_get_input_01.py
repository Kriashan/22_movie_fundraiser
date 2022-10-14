import unittest
import re


class TestMethods(unittest.TestCase):  # Class containing all the tests that will be run

#1672015237.8643615
 def test_not_blank_answer(self):
  not_wanted = ''
  self.assertNotEqual((testing_function := get_name('What is your name? ')), not_wanted, 'A blank output was returned')
  
#1672015230.7678998
 def test_validate_number_valid(self): # Test validate_number for a valid input with noise
  expected = 96
  test_input = '9a%@*&^j;\'6.'
  self.assertEqual((testing_function := validate_number(test_input)), expected, 'Did not get 96, expected 96')
 
#1672015230.7688968
 def test_validate_number_low(self): # Test validate_number for a lower than expected input
  expect_low = 'Value is too low'
  test_low = '0'
  self.assertEqual((testing_function := validate_number(test_low)), expect_low, 'Did not get Value is too low, expected Value is too low')
  
#1672015230.771313
 def test_validate_number_high(self): # Test validate_number for a higher than expected input
  expect_high = 'Value is too high'
  test_high = '100'
  self.assertEqual((testing_function := validate_number(test_high)), expect_high, 'Did not get Value is too high, expected Value is too high')
 
#1672015230.7723124
 def test_validate_number_invalid(self): # Test validate_number for an invalid input
  expect_invalid = 'Number invalid'
  test_invalid = 'Hello there!'
  self.assertEqual((testing_function := validate_number(test_invalid)), expect_invalid, 'Did not get Number invalid, expected Number invalid')
  

#1672015230.7723124
def ask_question(ask='') -> "Ask question until the answer is not blank":
 if (answer := input(ask)) != '' or print('Input cannot be blank') or (answer := ask_question(ask)) != '':
  return answer

#1672015230.7733104
def validate_number(number='', low_range=0, high_range=100):
 try:
  if  high_range > (answer := int(''.join(re.findall('[0-9]', number)))) > low_range:
   return answer
  elif high_range <= answer:
   return 'Value is too high'
  elif low_range >= answer:
   return 'Value is too low'
 except ValueError:
  return 'Number invalid'
# name = not_blank('What is your name?: '); print('Hello {}'.format(name))

if __name__ == '__main__':
 unittest.load_tests(TestMethods)
 unittest.main()
 
 
