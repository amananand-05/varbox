# Variable dumpper/encryptor 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.8.8](https://img.shields.io/badge/python-3.8.8-blue.svg)](https://www.python.org/downloads/release/python-388/) 

## Example 1

 ```
# test.py
import varbox
class Glass:
    def __init__(self):
        self.amount = "500ml"
    def set_amount(self,a):
        self.amount = a
    def get_amount(self):
        return self.amount

g = Glass()
varbox.dump(1, 2, 3, g, filepath="var_file_path", varnames=["a", "b", "c", "g"])
k = varbox.load("var_file_path")
print(k["g"].amount)
  ```

## Example 2

 ```
import cipher
from constants import encryptions
print("==============================================================")
key = "0000000000000000"
plain_text = "I am the secret message"
encrypted_string,iv = cipher.encrypt(encryptions.AES, plain_text, key)
decrypted_text = cipher.decrypt(encryptions.AES, encrypted_string, key, iv)

print("plain_text\t\t\t:\t"+plain_text)
print("key\t\t\t\t\t:\t"+key)
print("encrypted_string\t:\t"+encrypted_string)
print("iv\t\t\t\t\t:\t"+str(iv))
print("decrypted_text\t\t:\t"+decrypted_text)

print("==============================================================")
key = "0000000000000000"
plain_text = "I am the secret message"
encrypted_string,iv = cipher.encrypt(encryptions.BLOW_FISH, plain_text, key)
decrypted_text = cipher.decrypt(encryptions.BLOW_FISH, encrypted_string, key, iv)

print("plain_text\t\t\t:\t"+plain_text)
print("key\t\t\t\t\t:\t"+key)
print("encrypted_string\t:\t"+encrypted_string)
print("iv\t\t\t\t\t:\t"+str(iv))
print("decrypted_text\t\t:\t"+decrypted_text)
print("==============================================================")
key = "0000000000000000"
plain_text = "I am the secret message"
encrypted_string,iv = cipher.encrypt(encryptions.ARC4, plain_text, key)
decrypted_text = cipher.decrypt(encryptions.ARC4, encrypted_string, key, iv)

print("plain_text\t\t\t:\t"+plain_text)
print("key\t\t\t\t\t:\t"+key)
print("encrypted_string\t:\t"+encrypted_string)
print("iv\t\t\t\t\t:\t"+str(iv))
print("decrypted_text\t\t:\t"+decrypted_text)
  ```
