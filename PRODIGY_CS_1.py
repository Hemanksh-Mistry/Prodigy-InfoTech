# Task-01
# Implement Caesar Cipher
# Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

# Function to encrypt the text
def encrypt_text(text, shift):
        encrypted_text = ""
        for char in text:
                if char.isalpha():
                        ascii_val = ord(char)
                        if char.islower():
                                encrypted_text += chr((ascii_val - 97 + shift) % 26 + 97)
                        else:
                                encrypted_text += chr((ascii_val - 65 + shift) % 26 + 65)
                else:
                        encrypted_text += char
        return encrypted_text

# Function to decrypt the text
def decrypt_text(text, shift):
        decrypted_text = ""
        for char in text:
                if char.isalpha():
                        ascii_val = ord(char)
                        if char.islower():
                                decrypted_text += chr((ascii_val - 97 - shift) % 26 + 97)
                        else:
                                decrypted_text += chr((ascii_val - 65 - shift) % 26 + 65)
                else:
                        decrypted_text += char
        return decrypted_text

# Main Function
def main():
        #MENU
        print("MENU")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
                # Taking the text and shift value as input from the user
                text = input("Enter the text: ")
                shift = int(input("Enter the shift value: "))
                # Encrypting the text
                encrypted_text = encrypt_text(text, shift)
                print("Encrypted text: ", encrypted_text)
                main()

        elif choice == 2:
                # Taking the text and shift value as input from the user
                text = input("Enter the text: ")
                shift = int(input("Enter the shift value: "))
                # Decrypting the text
                decrypted_text = decrypt_text(text, shift)
                print("Decrypted text: ", decrypted_text)
                main()

        elif choice == 3:
                exit()

        else:
                print("Invalid choice")
                main()

# Calling the main function
if __name__ == "__main__":
        main()