import time

def countdown(num):
    while num >= 1:
        if  num > 1:
            print(f"{num} SECOND(S)!", end="\n")
            num -= 1

        else:
            print(f"{num} SECOND(S)!", end="\n")
            print(f"HAPPY NEW YEAR!")
            num -= 1

def countdown_with_sleep(num):
    while num >= 1:
        if  num > 1:
            print(f"{num} SECOND(S)!", end="\n")
            num -= 1
            time.sleep(1)

        else:
            print(f"{num} SECOND(S)!", end="\n")
            print(f"HAPPY NEW YEAR!")
            num -= 1