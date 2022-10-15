import sys
import csv
import re

# Asks the user a question until answer is not blank and is expected type
#review time: 1672092488.6429076
def ask_user_question(ask='', re_filter='', expected_type='str'):
    if (answer := ''.join(re.findall(re_filter, input(ask)))) != '': 
        if expected_type == 'str':
            answer = str(answer)
        elif expected_type == 'int':
            answer = int(answer)
        elif expected_type == 'float':
            answer = float(answer)
        else:
            stdout('Unknown type expected {0}, options are str, int, and float'.format(expected_type))
            return None
        return answer
    else:
        stdout('Input cannot be blank and must be type {0}'.format(expected_type))
        stdout('Input is: {0}'.format(answer))
    return ask_user_question(ask, re_filter, expected_type)

# Validate if the user age is greater than low_range and less than high_range
#review time: 1672092488.646927
def is_in_range(user_input='', low_range=12, high_range=130) -> bool:
    # Is user between low_range and high_range years old?
    if low_range >= int(str(user_input) + '0') // 10 <= high_range:
        return True
    return False

# Return True if seat available else return False
#review time: 1672092488.6488945
def seat_available(seats_available) -> bool:
    if seats_available > 0:
        return True
    return False

# Return True if seats_limit greater than seats_available else return False
#review time: 1672092488.649891
def seat_maximum(seats_available, seats_limit) -> bool:
    if seats_limit >= seats_available:
        return True
    return False

# Adds \n and uses the faster version of print
#review time: 1672094442.4970124
def stdout(text):
    sys.stdout.write(str(text) + '\n')
