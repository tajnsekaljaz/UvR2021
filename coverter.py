x = input("Binary to decimal:")
index = 0
rezultat = 0
for i in reversed(x):
    if index == 0 and int(i) == 1:
        rezultat += 1
        index += 1
    elif int(i) == 0:
        index += 1
    else:
        rezultat += 2 ** index
        index += 1
print(rezultat)

x = int(input("Decimal to binary: "))
l = []
while x != 0:
    if x % 2 == 0:
        l.append(0)
        x = round(x / 2)
    else:
        l.append(1)
        x = round((x / 2) - 0.5)
razultat = 0
stetje = 0
for i in (l):
    razultat += (i * 10**stetje)
    stetje += 1
print(razultat)

