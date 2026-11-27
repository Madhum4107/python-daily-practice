"""Student information and score conversion exercise."""

def score_out_of_ten(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    return score / 10

if __name__ == "__main__":
    name = input("Name: ").strip()
    department = input("Department: ").strip()
    try:
        score = float(input("Score (0-100): "))
        print(f"Name: {name}")
        print(f"Score: {score_out_of_ten(score):.1f}/10")
        print(f"Department: {department}")
    except ValueError as error:
        print(f"Invalid score: {error}")
