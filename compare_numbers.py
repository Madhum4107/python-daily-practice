"""Compare two user-entered integers."""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is greater")
elif b > a:
    print(f"{b} is greater")
else:
    print("Both numbers are equal")
