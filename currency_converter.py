currency=input("Which currency do you want to convert?\noptions: EUR or RSD ").upper().strip()
try:
    value=float(input("Enter the amount: "))
except ValueError:
    print("Invalid option. Please enter a valid number")
if value <= 0:
    print("Error: Number must be a positive and greater than zero.\n")
    
if currency == "RSD":
    print(value/117.5)
elif currency== "EUR":
    print(value*117.5)
