from morse import MORSE_TABLE


def to_morse_code(base_message: str) -> str:
    """
    Convert any string containing letters and numbers to a Morse code string.
    If any character cannot be translated it will be displayed as "*" .
    Parameters:
        base_message (str): Base string to convert to Morse Code

    Returns:
        encoded_message (str): Converted string
    """
    # Loop through all characters in base_message and check if it is a "space".
    # If the character is not a "space" then pick the corresponding value from MORSE_TABLE dict and add it to
    # encoded_message.
    # If no match found for the current character in MORSE_TABLE dict -> add "*" character to encoded_message.
    # Else just add a space to encoded_message.
    encoded_message = [f"{MORSE_TABLE.get(character, '*')} " if character != " " else " " for character in base_message]
    # If a character couldn't be encrypted display a message
    if "* " in encoded_message:
        print("Some characters couldn't be encrypted you will see '*' instead.")
    # Use join to return a string containing all encrypted characters.
    return "".join(encoded_message)


if __name__ == "__main__":
    message_to_encrypt = input("Text to convert to Morse Code: ").upper()
    result = to_morse_code(message_to_encrypt)
    print(f"Result: {result}")
