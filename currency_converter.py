currency=input("Which currency do you want to convert?\noptions: EUR or RSD ").upper().strip()
value=float(input("Enter the amount: "))
if currency == "RSD":
    print(value/117.5)
elif currency== "EUR":
    print(value*117.5)
