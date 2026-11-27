"""Pass/fail example with input range validation."""

def classify_mark(mark):
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100")
    return "Pass" if mark >= 35 else "Fail"

if __name__ == "__main__":
    try:
        mark = int(input("Enter mark (0-100): "))
        print(classify_mark(mark))
    except ValueError as error:
        print(error)
