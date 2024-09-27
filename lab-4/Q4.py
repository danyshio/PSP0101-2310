weight = int(input("Enter the weight in grams: "))
kg = weight // 1000
grams = weight % 1000

print(f"{weight} grams = {kg} kilograms {grams} grams")