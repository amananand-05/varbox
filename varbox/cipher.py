from encryption import arc4_encryption as arc, blowfish_encryption as bf, aes_encryption as aes
from constants import encryptions

def encrypt(algo_name, plain_text, key):
    '''
    :param plain_text: Plain text
    :param key: Encryption Key
    :param algo_name:  AES (Advanced Encryption Standard), BLOW_FISH (Blowfish Encryption Algorithm), ARC4 (Alleged RC4)
    :return: encrypted string and iv(if present)
    '''

    if algo_name.lower() == "aes":
        e = aes

    elif algo_name.lower() == "blow_fish":
        e = bf

    elif algo_name.lower() == "arc4":
        e = arc
        return e.encrypt(plain_text, key),None

    return e.encrypt(plain_text,key)


def decrypt(algo_name, encrypted_string, key, iv=None):
    '''
    :param plain_text: Plain text
    :param key: Encryption Key
    :param algo_name:  AES (Advanced Encryption Standard), BLOW_FISH (Blowfish Encryption Algorithm), ARC4 (Alleged RC4)
    :return: decrypted string
    '''

    if algo_name.lower() == "aes":
        d = aes

    elif algo_name.lower() == "blow_fish":
        d = bf

    elif algo_name.lower() == "arc4":
        d = arc
        return d.decrypt(encrypted_string, key)

    return d.decrypt(encrypted_string, key, iv)

'''
# Example: 

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
'''