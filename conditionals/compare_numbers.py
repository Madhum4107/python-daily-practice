"""Compare two numbers and return a clear result."""

def compare(a, b):
    if a > b:
        return f"{a} is greater"
    if b > a:
        return f"{b} is greater"
    return "Both numbers are equal"

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(compare(a, b))
