x = 49**7 + 7**21 - 7
y = ""

while x != 0:
        y = y + str(x % 7)
        x = x // 7

print(y.count("6"))
