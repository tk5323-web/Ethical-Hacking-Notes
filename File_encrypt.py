from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save the key
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Encrypt a message
message = b"Hello Ethical Hacking!"
encrypted = cipher.encrypt(message)
print("Encrypted:", encrypted)

# Decrypt the message
decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted.decode())
