# import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plain_text, key):
    print("aes encrypt")
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    encrypted_string = base64.b64encode(ct_bytes).decode('utf-8')
    return encrypted_string, iv

def decrypt(encrypted_string,key, iv):
    print("aes decrypt")
    cipher = AES.new(key.encode(), AES.MODE_CBC, base64.b64decode(iv))
    pt_bytes = unpad(cipher.decrypt(base64.b64decode(encrypted_string)), AES.block_size)
    return pt_bytes.decode('utf-8')

# Example usage
# key =   "0000000000000000" #should be atleast 16 and upto 32 bytes
# plain_text = "I am the secret message"
# encrypted_string,iv = encrypt(plain_text, key)
# decrypted_text = decrypt(encrypted_string, key, iv)
#
# print("plain_text\t\t\t:\t"+plain_text)
# print("key\t\t\t\t\t:\t"+key)
# print("encrypted_string\t:\t"+encrypted_string)
# print("iv\t\t\t\t\t:\t"+iv)
# print("decrypted_text\t\t:\t"+decrypted_text)


