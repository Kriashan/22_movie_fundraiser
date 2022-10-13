import ticket_price_library as ticket

if __name__ == '__main__':

    #print(ticketLibrary.is_a_seat_available())
    print(ticket.ask_user_question('What is your first name?', '[A-Za-z]', 'str'))
    print(ticket.ask_user_question('What is your age?', '[0-9]', 'int'))