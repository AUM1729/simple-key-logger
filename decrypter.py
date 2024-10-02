from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

try:
    # Load the encrypted text from the file
    with open("optimizerresult.txt", "rb") as f:
        encrypted_text = f.read()

    # Load the encryption key
    key = load_key()

    # Create a Fernet cipher object with the key
    cipher = Fernet(key)

    # Decrypt the encrypted text
    decrypted_text = cipher.decrypt(encrypted_text)

    # Convert the decrypted text to string and print it
    print(decrypted_text.decode())

except Exception as e:
    print("Decryption failed:", e)
