for i in range(1, 11):
    print(i)
a = 1
# Infinity loop
while True:
    if a >= 100:
        break
    print(f'{a:03}')
    a = a + 1
