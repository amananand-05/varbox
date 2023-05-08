from Crypto.Cipher import Blowfish
from Crypto import Random
import base64

def encrypt(plain_text, key):
    print("bf encrypt")
    key = key.encode()
    padded_plain_text = plain_text + ((Blowfish.block_size - len(plain_text) % Blowfish.block_size) * "\0")
    iv = Random.new().read(Blowfish.block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    encrypted_text = cipher.encrypt(padded_plain_text.encode())
    encrypted_text_b64 = base64.b64encode(encrypted_text).decode()
    iv_b64 = base64.b64encode(iv).decode()
    return f"{encrypted_text_b64}",f"{iv_b64}"

def decrypt(encrypted_string,key, iv):
    print("bf decrypt")
    key = key.encode()
    iv_b64 = iv
    encrypted_text_b64 = encrypted_string
    iv = base64.b64decode(iv_b64)
    encrypted_text = base64.b64decode(encrypted_text_b64)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    decrypted_text = decrypted_text.rstrip("\0")
    return decrypted_text


# Example usage
# key = "0000" #should be atleast 4 and upto 56 bytes
# plain_text = "I am the secret message"
# encrypted_string,iv = encrypt(plain_text, key)
# decrypted_text = decrypt(encrypted_string, key, iv)
#
# print("plain_text\t\t\t:\t"+plain_text)
# print("key\t\t\t\t\t:\t"+key)
# print("encrypted_string\t:\t"+encrypted_string)
# print("iv\t\t\t\t\t:\t"+iv)
# print("decrypted_text\t\t:\t"+decrypted_text)

