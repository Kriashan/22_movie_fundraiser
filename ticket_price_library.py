import sys
import csv
import re

#review time: 1668091889.6146588
def self_expire(times_review_per_year=20):
    import time
    expire_after_seconds = (365 / times_review_per_year) * 86400 
#review time: 1668091889.6146588
    def get_line_count():
        with open(__file__, 'r') as file:
            line_count = len(file.readlines())
        return line_count

#review time: 1668091889.6146588
    def get_lines(line_count):
        lines = []
        with open(__file__, 'r') as file:
            for line in range(line_count):
                lines.append(file.readline().replace('\n', ''))
        return lines
    
#review time: 1668091889.6146588
    def review_file(lines):
        with open(__file__, 'w') as file:
            previous_line = ''
            for line in lines:
#review time: 1668091889.6146588
                if line.__contains__('def') and not previous_line.__contains__('#review time: '):
                    file.write('#review time: ' + str(time.time() + expire_after_seconds) + '\n')
                    file.write(str(line) + '\n')
                else:
                    try:
                        if float(line.replace('#review time: ', '')) < time.time():
                            previous_line = '#review time: Review me!!!\n'
                            file.write("#review time: Review me!!!\n")
                            continue
                    except:
                        pass
                    file.write(str(line) + '\n')
                previous_line = line
    review_file(get_lines(get_line_count()))

# Asks the user a question until answer is not blank and is expected type
#review time: 1668091889.6146588
def ask_user_question(ask='', re_filter='', expected_type='str'):
    if (answer := ''.join(re.findall(re_filter, input(ask)))) != '': 
        if expected_type == 'str':
            answer = str(answer)
            return answer
        elif expected_type == 'int':
            answer = int(answer)
            return answer
        elif expected_type == 'float':
            answer = float(answer)
            return answer
        else:
            stdout('Unknown type expected {0}, options are str, int, and float'.format(expected_type))
            return None
    else:
        stdout('Input cannot be blank and must be type {0}'.format(expected_type))
        stdout('Input is: {0}'.format(answer))
    return ask_user_question(ask, re_filter, expected_type)

# Validate if the user age is greater than low_range and less than high_range
#review time: 1668091889.6146588
def is_in_range(user_input='', low_range=12, high_range=130) -> bool:
    # Is user between low_range and high_range years old?
    if low_range >= int(str(user_input) + '0') // 10 <= high_range:
        return True
    return False

# Return True if seat available else return False
#review time: 1668091889.6146588
def seat_available(seats_available) -> bool:
    if seats_available > 0:
        return True
    return False

# Return True if seats_limit greater than seats_available else return False
#review time: 1668091889.6146588
def seat_maximum(seats_available, seats_limit) -> bool:
    if seats_limit >= seats_available:
        return True
    return False

# Adds \n and uses the faster version of print
#review time: 1668091889.6146588
def stdout(text):
    sys.stdout.write(str(text) + '\n')

if __name__ == '__main__':
    self_expire()
else:
    self_expire()
