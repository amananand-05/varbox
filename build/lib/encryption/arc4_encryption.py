from Crypto.Cipher import ARC4
import base64

def encrypt(plain_text, key):
    print("arc4 encrypt")
    cipher = ARC4.new(key.encode(),ARC4.block_size)
    encrypted_message = cipher.encrypt(plain_text.encode())
    return base64.b64encode(encrypted_message).decode('utf-8')

def decrypt(encrypted_string,key):
    print("arc4 decrypt")
    cipher = ARC4.new(key.encode(),ARC4.block_size)
    pt_bytes = cipher.decrypt(base64.b64decode(encrypted_string))
    return pt_bytes.decode('utf-8')



# Example usage
# key = "0" #should be atleast 1 and upto 256 bytes
# plain_text = "I am the secret message"
# encrypted_string = encrypt(plain_text, key)
# decrypted_text = decrypt(encrypted_string, key)
#
# print("plain_text\t\t\t:\t"+plain_text)
# print("key\t\t\t\t\t:\t"+key)
# print("encrypted_string\t:\t"+encrypted_string)
# print("iv\t\t\t\t\t:\t"+"Not Applicable")
# print("decrypted_text\t\t:\t"+decrypted_text)
