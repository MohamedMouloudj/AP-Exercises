from decimal import Decimal
price=Decimal(input("Please type a price: "))
whole=price//1
frac=int(str(price%1).split(".")[1])
print(f"Dinars: {whole}\nCentimes : {frac}")