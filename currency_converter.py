RSD_TO_EUR_RATE = 117.5
print("Type EXIT at the currency prompt to exit program")
while True:
    currency=input("Which currency do you want to convert?\noptions: EUR or RSD ").upper().strip()
    if currency=="EXIT":
        print("Closing program..")
        break
    if currency not in ["EUR","RSD"]:
        print("Please enter a valid currency, or type EXIT.\n")
        continue
    while True:
        try:
            value=float(input("Enter the amount: "))
            if value <= 0:
                print("Error: Number must be a positive and greater than zero.\n")
                continue
            if currency == "RSD":
                converted=value/RSD_TO_EUR_RATE
                print(f"{value:,.2f} RSD is equal to {converted:,.2f} EUR")
            elif currency== "EUR":
                converted=value*RSD_TO_EUR_RATE
                print(f"{value:,.2f} EUR is equal to {converted:,.2f} RSD")
            break
        except ValueError:  
            print("Invalid option. Please enter a valid number")
            continue
