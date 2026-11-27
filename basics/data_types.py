"""Explore a Python value's type."""

def describe(value):
    return type(value).__name__

if __name__ == "__main__":
    sample = "madhu"
    print(describe(sample))
