import ticket_price_library as ticketHandler
import sys

#review time: 1672094442.4830754
def stdout(text):
    sys.stdout.write(str(text) + '\n')

if __name__ == '__main__':
    available_snacks = {
                        "Popcorn": {"Price": 2.50},
                        "M&M": {"Price": 3.00},
                        "Pita Chips": {"Price": 4.50},
                        "Orange juice": {"Price": 3.25},
                        "Water": {"Price": 2.00},
                       }

    ticket_brackets = {
                        15: {"Price": 7.50},
                        64: {"Price": 10.50},
                        65: {"Price": 6.50}
                      }

    #print(ticketLibrary.is_a_seat_available())
    stdout(ticketHandler.ask_user_question('What is your first name?', '[A-Za-z]', 'str'))
    stdout(ticketHandler.ask_user_question('What is your age?', '[0-9]', 'int'))
    stdout(ticketHandler.seat_maximum(151, 150)) # Seats_available, seats_limit
    stdout(ticketHandler.seat_maximum(-5, 150)) # Seats_available, seats_limit
    stdout(ticketHandler.seat_maximum(64, 150)) # Seats_available, seats_limit
    
    while True:
        wants_snacks = ticketHandler.ask_user_question('Do you want snacks? yes or no? ', '[a-z]', 'str')
        if wants_snacks == 'yes':
            while True:
                ask = 'What snacks do you want? The choices are: '
                for item in available_snacks:
                    ask += item + ': ${0} ea, '.format(available_snacks[item]['Price'])
                snackChoice = ticketHandler.ask_user_question(ask + ', or finish.\n', '[A-Za-z&]', 'str')
                if snackChoice == 'finish':
                    break
                if snackChoice in available_snacks: 
                    snackQuantity = ticketHandler.ask_user_question('What quantity of {0} would you like to order?'.format(snackChoice), '[0-9]', 'int')
                else:
                    stdout("That snack does not exist")
            stdout('Snacks have been ordered')
            break
        elif wants_snacks == 'no':
            stdout('Snacks have not been ordered')
            break
        stdout("Please input yes or no")
    
