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
    # Loop through all characters in message and check if it is a "space".
    # If the character is not a "space" then pick the corresponding value from MORSE_TABLE dict.
    # Else just add a space.
    # Use join to return a string containing all encrypted characters.
    encoded_message = [f'{MORSE_TABLE.get(character, "*")} ' if character != ' ' else ' ' for character in base_message]
    if '* ' in encoded_message:
        print("Some characters couldn't be encrypted you will see '*' instead.")
    return ''.join(encoded_message)


if __name__ == '__main__':
    message_to_encrypt = input('Text to convert to Morse Code: ').upper()
    result = to_morse_code(message_to_encrypt)
    print(f'Result: {result}')
