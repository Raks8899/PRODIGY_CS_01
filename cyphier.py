def caesar_cipher(text, shift, direction):
    result = ""

    # Adjust the shift direction based on encryption or decryption
    if direction == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Calculate the starting ASCII code depending on upper/lower case
            start = ord('A') if char.isupper() else ord('a')

            # Perform the shift
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            # Non-alphabet characters are added unchanged
            result += char

    return result


def main():
    while True:
        # Get user input
        direction = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
        if direction not in ["encrypt", "decrypt"]:
            print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift number: "))
        except ValueError:
            print("Shift must be a valid integer.")
            continue

        # Perform the encryption/decryption
        result = caesar_cipher(text, shift, direction)
        print(f"The {direction}ed message is: {result}")

        # Check if the user wants to continue
        again = input("Do you want to go again? Type 'yes' to continue, or any other key to exit: ").lower()
        if again != 'yes':
            break


if __name__ == "__main__":
    main()
