N = int(input("Enter N: "))

i = 1
while i <= N:
    print(i, end="")
    if i != N:
        print(", ", end="")
    i += 1