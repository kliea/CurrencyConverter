import sys
#Currency Converter
#get
USD = 0.01950059
PHP = 51.27050


while True:
    f = input("Enter Current Currency: ")
    g = input("Enter New Currency: ") 
    Amount = int(input("Enter Amount: "))

    if f == "PHP" and g == "USD":
        a = round(Amount * USD, 2)
        print(a)
        sys.exit()
    elif f == "USD" and g == "PHP":
        b = round(Amount * PHP, 2)
        print(b)
        sys.exit()
    else: 
        print("wrong input")