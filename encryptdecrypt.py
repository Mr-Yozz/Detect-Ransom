import os
import platform
from cryptography.fernet import Fernet
from load import loading
import pyfiglet

def generate_key():
    return Fernet.generate_key()

def load_key(key_path):
    with open(key_path, "rb") as key_file:
        return key_file.read()

def save_key(key, key_path):
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def encrypt_file(input_file, output_file, key):
    cipher = Fernet(key)
    with open(input_file, "rb") as file:
        data = file.read()
        encrypted_data = cipher.encrypt(data)
    with open(output_file, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    cipher = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

# Get the appropriate directory separator based on the platform
if platform.system() == "Windows":
    directory_separator = "\\"
else:
    directory_separator = "/"

# Example usage
def secure():
    # if __name__ == "__main__":
        # Generate or load the encryption key
        key_path = "key.key"
        try:
            key = load_key(key_path)
        except FileNotFoundError:
            key = generate_key()
            save_key(key, key_path)

        # Directory path
        print(pyfiglet.print_figlet(text="encrypt and decrypt",font="standard",colors="blue"))
        directory = input("\033[32m" "enter your path:")  # Change this to your directory path
        result = input("\033[32m" "encrypt or decrypt in your file")

        if str.lower(result) == "encrypt":
        # Encrypt all files in the directory
            loading()
            for filename in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, filename)):
                    input_file = os.path.join(directory, filename)
                    output_file = os.path.join(directory, filename + ".enc")
                    encrypt_file(input_file, output_file, key)
                    print("\033[32m"f"File '{filename}' encrypted successfully.")
        elif str.lower(result) == "decrypt":
        # Decrypt all encrypted files in the directory
            loading()
            for filename in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, filename)) and filename.endswith(".enc"):
                    input_file = os.path.join(directory, filename)
                    output_file = os.path.join(directory, filename[:-4])  # Remove the .enc extension
                    decrypt_file(input_file, output_file, key)
                    print("\033[32m"f"File '{filename}' decrypted successfully.")
        else:
            print("\033[1;31;40m""enter the correct option !!!""\033[0m")

# secure()