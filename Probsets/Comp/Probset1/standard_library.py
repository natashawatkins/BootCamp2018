import random
import sys
import math
import time
from box import *


if len(sys.argv) != 3:
    print("Exactly two extra command line arguments are required")
    print("System Arguments:", sys.argv)
    sys.exit()

numbers = list(range(1, 10))
time_limit = float(sys.argv[2])
start_time = time.time()

def play_round(numbers):
    
    if sum(numbers) < 6:
        roll = random.randint(1, 6)
    else:
        roll = random.randint(1, 6) + random.randint(1, 6)
        
    print(f"Seconds left: {time_limit - (round(time.time() - start_time))}")
    print(f"Roll: {roll}")
    
    if isvalid(roll, numbers):
        eliminate = input("Numbers to eliminate: ")
        choices = parse_input(eliminate, numbers)
        while len(choices) == 0:
            print("Invalid input")
            print(f"Seconds left: {time_limit - (round(time.time() - start_time))}")
            eliminate = input("Numbers to eliminate: ")
            choices = parse_input(eliminate, numbers)
        if sum(choices) == roll:
            for i in choices:
                numbers.remove(i)
        else:
            isvalid(roll, numbers)
    else:
        print("Game over!")
        end_game(numbers)
        
def end_game(numbers):
    print(f"Score for player {sys.argv[1]}: {sum(numbers)}")
    print(f"Time played: {round(time.time() - start_time, 2)}")
    if len(numbers) == 0:
        print("Congratulations!! You shut the box!")
    else:
        print("Better luck next time >:")
    sys.exit()

while len(numbers) > 0:
    print(f"Numbers left: {numbers}")
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("Game over!")
        end_game(numbers)
    play_round(numbers)
    
end_game(numbers)