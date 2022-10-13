import ticket_price_library as ticket

if __name__ == '__main__':
    ticketLibrary = ticket.TicketSystem(seats_available=150)

    #print(ticketLibrary.is_a_seat_available())
    print(ticketLibrary.ask_user_question('Am I cute?', '[A-Za-z]'))