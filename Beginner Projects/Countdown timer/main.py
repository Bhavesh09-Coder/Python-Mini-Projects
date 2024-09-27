## Project title : countdown timer

 

import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # The '\r' updates the same line in the console
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Example usage: Set the countdown for 10 seconds
seconds = int(input("Enter the time in seconds: "))
countdown_timer(seconds)
