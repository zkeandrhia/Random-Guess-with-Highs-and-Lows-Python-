import random

number = 0
count_of_guess = 0
user = random.randint(1, 15)
print('Guessing number from 1-15. Type "Stop" If you want to end the guess\n')

while number != "Stop" and number != user:
    number = input('Enter your guess: ')
    
    if number == "Stop":
        break
    
    number = int(number) # converting str into int
    count_of_guess += 1 #number of tries
    
    if number > user:
        print("Too high!")
        
    elif number < user:
        print("Too low!")
        
    else:
        print(f'You got the number in {count_of_guess} tries! Great Job!')