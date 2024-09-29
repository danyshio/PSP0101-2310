package = int(input("Enter package no: "))

if (package == 1):
    minutes = int(input("Enter minutes used: "))
    if minutes <= 450:
        amount = 40
        print(f"Amount due = RM{amount}")
    else:
        amount = 40 + ((minutes - 450) * 0.45)
        print(f"Amount due = RM{amount}")

elif (package == 2):
    minutes = int(input("Enter minutes used: "))
    if minutes <= 900:
        amount = 60
        print(f"Amount due = RM{amount}")
    else:
        amount = 60 + ((minutes - 900) * 0.4)
        print(f"Amount due = RM{amount}")

elif (package == 3):
    print("Amount due = RM70")



