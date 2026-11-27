"""Branch based on a user-entered status string."""

def status_message(status):
    if status.strip().lower() == "finished":
        return "The task is finished."
    return "The task is still in progress."

if __name__ == "__main__":
    status = input("Enter status (finished/in progress): ")
    print(status_message(status))
