"""Illustrative if/else branch using a match result."""

def match_message(result):
    if result.strip().lower() == "win":
        return "Ee sala cup namdhe!"
    return "Better luck next time."

if __name__ == "__main__":
    result = input("Enter match result (win/other): ")
    print(match_message(result))
