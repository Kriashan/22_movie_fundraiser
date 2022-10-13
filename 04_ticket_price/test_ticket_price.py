import ticket_price_library as ticketHandler
import sys

if __name__ == '__main__':
    available_snacks = {
                        "Popcorn": {"Price": 2.50},
                        "M&M": {"Price": 3.00},
                        "Pita Chips": {"Price": 4.50},
                        "Orange juice": {"Price": 3.25},
                        "Water": {"Price": 2.00},
                       }

    #print(ticketLibrary.is_a_seat_available())
    print(ticketHandler.ask_user_question('What is your first name?', '[A-Za-z]', 'str'))
    print(ticketHandler.ask_user_question('What is your age?', '[0-9]', 'int'))
    print(ticketHandler.seat_maximum(151, 150)) # Seats_available, seats_limit
    print(ticketHandler.seat_maximum(-5, 150)) # Seats_available, seats_limit
    print(ticketHandler.seat_maximum(64, 150)) # Seats_available, seats_limit
    
    while True:
        wants_snacks = ticketHandler.ask_user_question('Do you want snacks? yes or no?', '[a-z]', 'str')
        if wants_snacks == 'yes':
            sys.stdout.write('Snacks have been ordered')
            break
        elif wants_snacks == 'no':
            sys.stdout.write('Snacks have not been ordered')
            break
    