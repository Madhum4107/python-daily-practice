"""Branch using a value entered by the user."""
status = input("Enter status (finished/other): ").strip().lower()
if status == "finished":
    print("Task completed.")
else:
    print("Task still in progress.")
