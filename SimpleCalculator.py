import math
def welcome():
    print('''
Welcome to Ariana's  Calculator
''')
...
welcome()

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+  for addition
-  for subtraction
*  for multiplication
/  for division
** for square
/- for square root
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '**':
        sqr = number_1**2
        print(number_1 * number_1)

    elif operation == '/-':
        sqr = math.sqrt(number_1)
        print("The square root of ", number_1, "Is ", sqr)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Goodbye.')
    else:
        again()

calculate()

