# Project 15: Countdown Timer

import time

seconds = int(input("Enter seconds to count down: "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)

print("Time's up!")
