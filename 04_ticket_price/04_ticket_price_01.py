import unittest
import csv
import re


class TicketSystem:
    def __init__(self) -> None:
        pass


    # Return True if there is a seat available
    def is_a_seat_available(available_seats = 0) -> bool:
        if available_seats > 0:
            return True
        return False


    # Return the users name
    def get_user_name(self) -> str:
        return self.ask_question('What is your first name?', '[a-zA-Z]')

    # Return the users age
    def get_user_age(self, min_age=12, max_age=130) -> int:
        if self.validate_age(response := self.ask_question('What is your age?', '[0-9]'), min_age, max_age):
            return response
        print("Your age must be an integer between {} and {}".format(min_age, max_age))
        return self.get_user_age(min_age, max_age)


    # Ask question until the answer is not blank
    def ask_question(self, ask='', valid_characters='') -> str:
        if (answer := (''.join(re.findall(valid_characters, input(ask))))) != '':
            return answer
        print('Input cannot be blank {}'.format(answer))
        return self.ask_question(ask, valid_characters)


    # Validate if the users age is valid
    def validate_age(self, number='', low_range=12, high_range=130) -> int:
        # add 0 so no blank and divide by 10 to remove shifting
        if high_range > (answer := (int((''.join(re.findall('[0-9]', number)) + '0')) // 10)) > low_range:
            return True
        return False
