i = 1
while i <= 10:
    print(i)
    i = i + 1

a = 1
# Infinity loop
while True:
    if a >= 100:
        break
    print(f'{a:03}')
    a = a + 1
