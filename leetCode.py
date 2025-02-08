x = int(input("Masukan X :"))
y = int(input("Masukan Y"))
i = 0
while x != y:
    if x%2 == 0:
        x = x//2
        i += 1
    else:
        x -= 1
        i += 1
print(i)