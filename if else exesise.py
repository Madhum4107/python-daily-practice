"""Pass/fail example with a valid mark range."""
mark = int(input("Enter mark (0-100): "))
if not 0 <= mark <= 100:
    print("Mark must be between 0 and 100")
elif mark >= 35:
    print("Pass")
else:
    print("Fail")
