import unittest
import sys
import csv
import re


class TicketSystem:
    def __init__(self, seats_available=150) -> None:
        self.seats_available = seats_available

    # Return True if there is a seat available
    def is_a_seat_available(self) -> bool:
        if self.seats_available > 0:
            return True
        return False

    # Return the users name
    def ask_user_for_first_name(self) -> str:
        return self.ask_user_question('What is your first name?', '[a-zA-Z]')

    # Return the users age
    def ask_user_for_age(self, min_user_age=12, max_user_age=130) -> int:
        if self.is_number_in_range(user_answer := 
                                self.ask_user_question('What is your age?',
                                '[0-9]'),
                                min_user_age,
                                max_user_age):
            return user_answer
        sys.stdout.write("Your age must be an integer between {0} and {1}".format(min_user_age, max_user_age))
        return self.ask_user_for_age(min_user_age, max_user_age)

    # Ask question until the answer is not blank
    def ask_user_question(self, question='', regex_character_filter='') -> str:
        if (answer := ''.join(re.findall(regex_character_filter, input(question)))) != '':
            return answer
        sys.stdout.write('Input cannot be blank')
        return self.ask_user_question(question, regex_character_filter)

    # Validate if the user age is greater than low_range and less than high_range
    def is_number_in_range(self, user_input='', low_range=12, high_range=130) -> int:
        # Is user between low_range and high_range years old?
        if int(str(user_input) + '0') // 10 in range(low_range+1, high_range):
            return True
        return False
