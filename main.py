from ProjectMath import *
import os

def main():
    while True:
        os.system('cls')

        action = input('Enter action(+, -) --> ')

        a = float(input('Enter first number --> '))
        b = float(input('Enter second number --> '))

        if action == '+':
            answer = plus(a, b)
        
        elif action == '-':
            answer = minus(a, b)

        else:
            print('Incorrect action!')
            answer = 'none'

        print(f'The answer is {answer}.')

        input('Press Enter to continue ... ')



if __name__ == '__main__':

    main()
