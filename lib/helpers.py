def print_header(title):
    """Print a formatted header for sections."""
    border = "=" * (len(title) + 4)
    print(f"\n{border}\n  {title}\n{border}")

def print_list(items, item_name="Item"):
    """Print a list of items, or a message if the list is empty."""
    if not items:
        print(f"No {item_name.lower()}s found.")
        return
    for item in items:
        print(item)

def get_int_input(prompt_text):
    """Prompt the user for an integer, and keep asking until a valid number is entered."""
    while True:
        user_input = input(prompt_text)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Please enter a valid number.")

def confirm_action(prompt_text="Are you sure? (y/n): "):
    """Prompt the user to confirm an action with yes or no."""
    while True:
        choice = input(prompt_text).strip().lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")