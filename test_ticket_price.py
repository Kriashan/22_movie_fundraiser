import ticket_price_library as ticketHandler
import pandas
import csv

#review time: 1672184810.1298804
def order_snacks(user_name, user_age, order):

    available_snacks = {
                    "Popcorn": {"Price": 2.50, "Profit": 0.5},
                    "M&M": {"Price": 3.00, "Profit": 0.60},
                    "Pita_chips": {"Price": 4.50, "Profit": 0.90},
                    "Orange juice": {"Price": 3.25, "Profit": 0.65},
                    "Water": {"Price": 2.00, "Profit": 0.40},
                    }
    
    ticket_brackets = {
                    15: {'Price': 7.50, 'Profit': 2.50},
                    64: {'Price': 10.50, 'Profit': 5.50},
                    150: {'Price': 6.50, 'Profit': 1.50}
                    }

    order['Name'].append(user_name)
    order['Age'].append(user_age)
    order['Popcorn'].append(0)
    order['M&M'].append(0)
    order['Pita_chips'].append(0)
    order['Orange juice'].append(0)
    order['Water'].append(0)
    order['Price'].append(0)
    order['Profit'].append(0)

    for age in ticket_brackets:
        if user_age < age:
            order['Price'][len(order['Price'])-1] += ticket_brackets[age]['Price']
            order['Profit'][len(order['Profit'])-1] += ticket_brackets[age]['Profit']
            break

    while True:
        wants_snacks = ticketHandler.ask_user_question('Do you want snacks? yes or no? ', '[a-z]', 'str')
        if wants_snacks == 'yes':
            while True:
                ask = 'What snacks do you want? The choices are: '
                for item in available_snacks:
                    ask += item + ': ${0:.2f} ea, '.format(available_snacks[item]['Price'])
                snackChoice = ticketHandler.ask_user_question(ask + 'or finish.\n', '[A-Za-z&]', 'str')
                if snackChoice == 'finish':
                    break
                if snackChoice in available_snacks: 
                    snackQuantity = ticketHandler.ask_user_question('What quantity of {0} would you like to order?'.format(snackChoice), '[0-9]', 'int')
                    ticketHandler.stdout('Added {0} {1} to your order'.format(snackQuantity, snackChoice))
                    ticketHandler.stdout('Added price: ${0:.2f}'.format(available_snacks[snackChoice]['Price'] * snackQuantity))
                    ticketHandler.stdout('Profit: ${0:.2f}'.format(available_snacks[snackChoice]['Profit'] * snackQuantity))
                    if order[snackChoice][len(order[snackChoice])-1] + snackQuantity >= 0:
                        order[snackChoice][len(order[snackChoice])-1] += snackQuantity
                        order['Price'][len(order['Price'])-1] += available_snacks[snackChoice]['Price'] * snackQuantity
                        order['Profit'][len(order['Profit'])-1] += available_snacks[snackChoice]['Profit'] * snackQuantity
                    else:
                        ticketHandler.stdout('You can not order negative {0}'.format(snackChoice))
                    data = pandas.DataFrame(order)
                    
                    data.to_csv("data.csv")
                    ticketHandler.stdout(data) 
                else:
                    ticketHandler.stdout('That snack does not exist')
            while True:
                payment = ticketHandler.ask_user_question('Will you be paying with cash or card?', '[a-z]', 'str')
                if payment == 'cash':
                    break
                elif payment == 'card':
                    order['Price'][len(order['Price'])-1] *= 1.05
                    break
                else:
                    ticketHandler.stdout('Please choose cash or card')
            ticketHandler.stdout('Snacks have been ordered')
            ticketHandler.stdout('Final cost comes to ${0:.2f}'.format(order['Price'][len(order['Price'])-1]))
            break
        elif wants_snacks == 'no':
            while True:
                payment = ticketHandler.ask_user_question('Will you be paying with cash or card?', '[a-z]', 'str')
                if payment == 'cash':
                    break
                elif payment == 'card':
                    order['Price'][len(order['Price'])-1] *= 1.05
                    break
                else:
                    ticketHandler.stdout('Please choose cash or card')
            ticketHandler.stdout('Snacks have been ordered')
            ticketHandler.stdout('Snacks have not been ordered')
            ticketHandler.stdout('Final cost comes to ${0:.2f}'.format(order['Price'][len(order['Price'])-1]))
            break
        ticketHandler.stdout('Please input yes or no')
    return order


if __name__ == '__main__':
    pandas.options.display.max_rows = 9999
    tickets_available = 150

    order = {'Name': [],
                'Age': [],
                'Popcorn': [],
                'M&M': [],
                'Pita_chips': [],
                'Orange juice': [],
                'Water': [],
                'Price': [],
                'Profit': [] 
                } # Name, age, Popcorn, M&M, etc, final_cost, profit

    while True:
        ticketHandler.stdout('{0} tickets available'.format(tickets_available))
        if ticketHandler.seat_available(tickets_available):
            user_name = ticketHandler.ask_user_question('What is your first name?', '[A-Za-z]', 'str')
            user_age = ticketHandler.ask_user_question('What is your age?', '[0-9]', 'int')
            if ticketHandler.is_in_range(user_age):
                ticketHandler.stdout('Unfortunately you are not within the age range required for this movie')
                continue
            order = order_snacks(user_name, user_age, order)
            tickets_available -= 1
        else:
            ticketHandler.stdout("Sorry we are sold out")
            break

        
