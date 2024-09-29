N = int(input("Enter N: "))

i = 1
while i <= N:
    print(i, end="")
    if i != N: #we check not last item to decide whether to show ", "
        print(", ", end="")
    i += 1


#method 2

N = int(input("Enter N: "))

for i in range(N):
    print(i+1, end="")
    if i+1 != N:
        print(", ", end="")