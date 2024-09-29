N = int(input("Enter N: "))

i = 1 
while i <=  N:
    if i%2 == 0:
        print(i, end="")
        if i != N:
            print(", ", end="")
    i += 1


#method 2

N = int(input("Enter N: "))

for i in range(N):
    if (i+1)%2 == 0:
        print(i+1, end="")
        if i != N:
            print(", ", end="")
    i+=1