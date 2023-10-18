"""
Question 4
This function will crate an addition problem for the user to solve. The problem will pick two random nunbers between 100 and 999.
The program will let you know the problem and will let the user solve it. If guessed correctly, the program will tell you that
problem is correct and how many correct questions you have gotten in a row. If the user answered wrong, it will tell the user
with the correct answer; the correct counts will go back to 0. After the user gets 3 correct answers in a row, the program will
tell the user and end the game. 

"""

import random

def math_game():
    #randomly generate two three digit numbers for the problem
    number_1 = random.randint(100,999)
    number_2 = random.randint(100,999)
    return number_1, number_2

def main():
    correct = 0 #start correct streak count

    while correct < 3:
        number_1, number_2 = math_game()
        correct_answer = number_1 + number_2
        print(f'What is {number_1} + {number_2}?') #program prints the question
        answer = int(input()) #user inputs their answer
       
        if answer == correct_answer:
            correct += 1
            print(f'You have answered {correct} in a row!')
        else:
            correct = 0
            print(f'Wrong! The correct ansewr is {correct_answer}.')
    print('Congratulations! You did a great job!')


if __name__ == "__main__":
    main()
