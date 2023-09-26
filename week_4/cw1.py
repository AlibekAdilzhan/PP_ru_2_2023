c = 0

while True:
    x = int(input())
    if x == 0:
        break
    if x % 2 != 0:
        c = c + 1

print(c)