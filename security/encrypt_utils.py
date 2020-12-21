
from cryptography.fernet import Fernet



# cipher which describes how to convert plantext to ciphertext and back.
CIPHER = {"a":"z", "A":"Z", "b":"a"}

def encrypt(plaintext: str):
    """substitution cipher"""
    return "".join(CIPHER.get(letter) for letter in plaintext)


DECIPHER = {v: k for k, v in CIPHER.items()}

def decrypt(ciphertext: str):
    """substitution decipher"""
    return "".join(DECIPHER.get(letter) for letter in ciphertext)


if __name__ == "__main__":
    # plaintext= "abA"
    # ciphertext = encrypt(plaintext)
    # print(f"The ciphertext: {ciphertext}")
    # print(f"The decrypted text: {decrypt(ciphertext)}")

    key = Fernet.generate_key()
    print(key)
    mycipher = Fernet(key)
    ciphertext = mycipher.encrypt(b"fluffy tail")
    print(ciphertext)