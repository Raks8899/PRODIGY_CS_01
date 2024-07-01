# # Caesar Cipher Encryption and Decryption

This is a Python script that implements a simple Caesar cipher encryption and decryption algorithm. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Usage

1. Run the `caesar_cipher.py` script.
2. You will be prompted to enter a message and a shift value.
3. The script will then encrypt the message using the provided shift value and print the encrypted message (cipher text) along with the original message, shift value, and decrypted message.

## Functions

- `encrypt(text, s)`: Encrypts the input text using the Caesar cipher with the given shift value `s`.
- `decrypt(text, s)`: Decrypts the input text using the Caesar cipher with the given shift value `s`.

## Example

```python
Enter Message: Hello World
Enter shift value: 3
Text: Hello World
Shift: 3
Cipher Text: Khoor Zruog
Decrypted Text: Hello World
