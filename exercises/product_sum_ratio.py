"""Calculate the product divided by the sum of three values."""

def product_to_sum_ratio(a, b, c):
    total = a + b + c
    if total == 0:
        raise ZeroDivisionError("The sum of inputs cannot be zero")
    return (a * b * c) / total

if __name__ == "__main__":
    try:
        values = [float(input(f"Enter number {i}: ")) for i in range(1, 4)]
        print(product_to_sum_ratio(*values))
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError as error:
        print(error)
