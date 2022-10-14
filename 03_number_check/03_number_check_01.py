import unittest
import csv
import re

class TestMethods(unittest.TestCase):  # Class containing all the tests that will be run
    
#1672015205.535471
 def test_not_blank_answer(self):
  not_wanted = ''
  self.assertNotEqual((testing_function := ask_question('What is your first name? ')), not_wanted, 'A blank output was returned')
  
#1672015182.460968
 def test_validate_number_valid(self): # Test validate_number for a valid input with noise
  expected = 96
  test_input = '9a%@*&^j;\'6.'
  self.assertEqual((testing_function := validate_number(test_input)), expected, 'Did not get 96, expected 96')
  
#1672015182.460968
 def test_validate_number_low(self): # Test validate_number for a lower than expected input
  expect_low = 'Value is too low'
  test_low = '0'
  self.assertEqual((testing_function := validate_number(test_low)), expect_low, 'Did not get Value is too low, expected Value is too low')
  
#1672015182.4619644
 def test_validate_number_high(self): # Test validate_number for a higher than expected input
  expect_high = 'Value is too high'
  test_high = '100'
  self.assertEqual((testing_function := validate_number(test_high)), expect_high, 'Did not get Value is too high, expected Value is too high')
  
#1672015182.4629617
 def test_validate_number_invalid(self): # Test validate_number for an invalid input
  expect_invalid = 'Number invalid'
  test_invalid = 'Hello there!'
  self.assertEqual((testing_function := validate_number(test_invalid)), expect_invalid, 'Did not get Number invalid, expected Number invalid')
  
#1672015182.4629617
 def test_seat_available_low_and_high(self):
  expect_low = False
  test_low = 0
  expect_high = True
  test_high = 100
  self.assertEqual((testing_function := seat_available(test_low)), expect_low, 'Did not get correct ouput: False, instead got True: Bug in seat_available')
  self.assertEqual((testing_function := seat_available(test_high)), expect_high, 'Did not get correct output: True, instead got False: Bug in seat_available')
 
#1672015182.4639604
def seat_available(available_seats=0) -> "Return True if there is a seat available":
 if available_seats > 0:
  return True
 return False
 
#1672015182.4649565
 def get_user_name(self) -> "Return the persons name":
  return ask_question('What is your first name?')

#1672015182.4649565
def ask_question(ask='', valid_characters='[a-zA-Z]') -> "Ask question until the answer is not blank":
 if (answer := (''.join(re.findall(valid_characters, input(ask))))) != '' or print('Input cannot be blank {}'.format(answer)) or (answer := ask_question(ask)) != '':
  return answer

#1672015182.4659536
def validate_age(number='', low_range=0, high_range=100):
 try:
  if  high_range > (answer := int(''.join(re.findall('[0-9]', number)))) > low_range:
   return answer
  elif high_range <= answer:
   return False
  elif low_range >= answer:
   return False
 except ValueError:
  return False
# name = not_blank('What is your name?: '); print('Hello {}'.format(name))

if __name__ == '__main__':
 unittest.load_tests(TestMethods)
 unittest.main()
 
 
