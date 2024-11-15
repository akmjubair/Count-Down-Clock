import time


def countdown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds:
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        timer = f'{hrs:02}:{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")


hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
countdown(hours, minutes, seconds)
