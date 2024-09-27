balance = float(input("Enter balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if balance > withdraw:
    print(f"New balance = {balance - withdraw}")
else:
    print("Withdrawal denied")