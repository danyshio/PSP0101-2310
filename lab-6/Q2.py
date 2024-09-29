N = int(input("Enter N: "))

i = 1 
while i <=  N:
    if i%2 == 0:
        print(i, end="")
        if i != N:
            print(", ", end="")
    i += 1