import time

num = 0
while True:
    if not num:
        print(1)
        num = 1
    else:
        print(0)
        num = 0
    time.sleep(1)
