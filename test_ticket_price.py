import ticket_price_library as ticketHandler
import pandas
import csv

#review time: 1672180488.330147
def order_snacks(user_name, user_age):
    available_snacks = {
                    "Popcorn": {"Price": 2.50, "Profit": 0.5},
                    "M&M": {"Price": 3.00, "Profit": 0.60},
                    "Pita Chips": {"Price": 4.50, "Profit": 0.90},
                    "Orange juice": {"Price": 3.25, "Profit": 0.65},
                    "Water": {"Price": 2.00, "Profit": 0.40},
                    }

    ordered_snacks = {'Name': [],
                      'Age': [],
                      'Popcorn': [],
                      'M&M': [],
                      'Pita Chips': [],
                      'Orange juice': [],
                      'Water': [],
                      'Price': [],
                      'Profit': [] 
                     } # Name, age, Popcorn, M&M, etc, final_cost, profit

    ordered_snacks['Name'].append(user_name)
    ordered_snacks['Age'].append(user_age)
    ordered_snacks['Popcorn'].append(0)
    ordered_snacks['M&M'].append(0)
    ordered_snacks['Pita Chips'].append(0)
    ordered_snacks['Orange juice'].append(0)
    ordered_snacks['Water'].append(0)
    ordered_snacks['Price'].append(0)
    ordered_snacks['Profit'].append(0)


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
                    if ordered_snacks[snackChoice][len(ordered_snacks[snackChoice])-1] + snackQuantity >= 0:
                        ordered_snacks[snackChoice][len(ordered_snacks[snackChoice])-1] += snackQuantity
                        ordered_snacks['Price'][len(ordered_snacks['Price'])-1] += available_snacks[snackChoice]['Price'] * snackQuantity
                        ordered_snacks['Profit'][len(ordered_snacks['Profit'])-1] += available_snacks[snackChoice]['Profit'] * snackQuantity
                    else:
                        ticketHandler.stdout('You can not order negative {0}'.format(snackChoice))
                    ticketHandler.stdout(ordered_snacks)
                else:
                    ticketHandler.stdout('That snack does not exist')
            ticketHandler.stdout('Snacks have been ordered')
            break
        elif wants_snacks == 'no':
            ticketHandler.stdout('Snacks have not been ordered')
            break
        ticketHandler.stdout('Please input yes or no')


if __name__ == '__main__':

    ticket_brackets = {
                        15: {"Price": 7.50},
                        64: {"Price": 10.50},
                        65: {"Price": 6.50}
                      }

    while True:
        user_name = ticketHandler.ask_user_question('What is your first name?', '[A-Za-z]', 'str')
        user_age = ticketHandler.ask_user_question('What is your age?', '[0-9]', 'int')
        snacks_ordered = order_snacks(user_name, user_age)

        
