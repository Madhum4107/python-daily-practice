"""Basic if/else branch example."""

def choose_message(is_true):
    return "Yes" if is_true else "No"

if __name__ == "__main__":
    print(choose_message(False))
