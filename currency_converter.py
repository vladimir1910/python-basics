print("Type EXIT at the currency prompt to exit program")
while True:
    currency=input("Which currency do you want to convert?\noptions: EUR or RSD ").upper().strip()
    if currency=="EXIT":
        print("Closing program..")
        break
    if currency not in ["EUR","RSD"]:
        print("Please enter a valid currency, or type EXIT.\n")
        continue
    try:
        value=float(input("Enter the amount: "))
    except ValueError:
        print("Invalid option. Please enter a valid number")
    if value <= 0:
        print("Error: Number must be a positive and greater than zero.\n")
        continue
    if currency == "RSD":
        print(value/117.5)
    elif currency== "EUR":
        print(value*117.5)
