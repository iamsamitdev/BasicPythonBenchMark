i = 1
while i <= 100:
    if i % 10 == 0:
        print(f'{i:03}')
    else:
        print(f'{i:03}', end=" ")
    i = i + 1
