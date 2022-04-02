from ProjectMath import *
import os


# Main function
def main():

    # Main cycle
    while True:

        # Console clear
        os.system('cls')

        # Enter action and numbers
        action = input('Enter action(+, -) --> ')

        a = float(input('Enter first number --> '))
        b = float(input('Enter second number --> '))

        # Check action
        if action == '+':
            answer = plus(a, b)
        
        elif action == '-':
            answer = minus(a, b)

        # If entered action isn't + or -, print Incorrect action.
        else:
            print('Incorrect action!')
            answer = 'none'

        # Print answer
        print(f'The answer is {answer}.')

        input('Press Enter to continue ... ')



if __name__ == '__main__':

    # Call main function
    main()
