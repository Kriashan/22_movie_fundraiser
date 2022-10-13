import sys
import csv
import re

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
        sys.stdout.write('Input is: {0}\n'.format(answer))
    return ask_user_question(ask, re_filter, expected_type)

# Validate if the user age is greater than low_range and less than high_range
def is_in_range(user_input='', low_range=12, high_range=130) -> bool:
    # Is user between low_range and high_range years old?
    if low_range >= int(str(user_input) + '0') // 10 <= high_range:
        return True
    return False

# Return True if seat available else return False
def seat_available(seats_available) -> bool:
    if seats_available > 0:
        return True
    return False

# Return True if seats_limit greater than seats_available else return False
def seat_maximum(seats_available, seats_limit) -> bool:
    if seats_limit >= seats_available:
        return True
    return False
