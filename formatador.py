def remove_spaces_and_dots(string):
    """
    Removes spaces and dots from the given string.
    """
    return string.replace(" ", "").replace(".", "")


def main():
    """
    Main function for the terminal app.
    """
    print("Welcome to the String Modifier App!")
    while True:
        user_input = input("Enter a string (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting...")
            break
        modified_string = remove_spaces_and_dots(user_input) + ".py"
        print("Modified string:", modified_string)


if __name__ == "__main__":
    main()
