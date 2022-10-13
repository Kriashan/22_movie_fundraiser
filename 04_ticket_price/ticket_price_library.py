import sys
import csv
import re


# Return True if seat available else return False
def seat_available(seats_available) -> bool:
    if seats_available > 0:
        return True
    return False

# Asks the user a question until answer is not blank and is expected type
def ask_user_question(ask='', re_filter='', expected_type='str'):
    if (answer := ''.join(re.findall(re_filter, input(ask)))) != '': 
        if expected_type == 'str':
            answer = str(answer)
        elif expected_type == 'int':
            answer = int(answer)
        elif expected_type == 'float':
            answer = float(answer)
        else:
            sys.stdout.write('Unknown type expected {0}, options are str, int, and float\n'.format(expected_type))
            return None
        return answer
    else:
        sys.stdout.write('Input cannot be blank and must be type {0}\n'.format(expected_type))
    return ask_user_question(ask, re_filter, expected_type)

# Validate if the user age is greater than low_range and less than high_range
def is_number_in_range(user_input='', low_range=12, high_range=130) -> int:
    # Is user between low_range and high_range years old?
    if int(str(user_input) + '0') // 10 in range(low_range+1, high_range):
        return True
    return False

