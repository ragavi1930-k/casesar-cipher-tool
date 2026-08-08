def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char

    return result


while True:

    print("\n" + "=" * 40)
    print("      Caesar Cipher Tool")
    print("=" * 40)

    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\n----- Encryption -----")

        message = input("Enter the message: ")
        shift = int(input("Enter shift value (1-25): "))

        encrypted = encrypt(message, shift)

        print("\nEncrypted Message:")
        print(encrypted)

    elif choice == "2":

        print("\n----- Decryption -----")

        message = input("Enter the encrypted message: ")
        shift = int(input("Enter shift value (1-25): "))

        decrypted = decrypt(message, shift)

        print("\nDecrypted Message:")
        print(decrypted)

    elif choice == "3":

        print("\nThank you for using Caesar Cipher Tool!")
        break

    else:
        print("\nInvalid Choice! Please try again.")