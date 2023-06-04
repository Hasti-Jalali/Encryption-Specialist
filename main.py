import os
import pbkdf2
import pyaes
import binascii
import secrets

def reduceKey():
    # get encryption key from file
    file = open("./Text Files/Encryption Key.txt", "r") # open the file in read mode
    key = file.read() # read the file
    salt = os.urandom(16) # generate a random 16 byte salt
    key = pbkdf2.PBKDF2(key, salt).read(32) # reduce the key to 32 bytes
    file.close() # close the file
    
    file = open("./Text Files/Salted Key.txt", "wb") # open the file in write mode
    file.write(binascii.hexlify(key)) # write the reduced key to the file
    file.close() # close the file

    iv = secrets.randbits(256) # generate a random 256 bit number

    return key, iv # return the key

def encrypt(key, iv):

    print("Encryption Key: ", binascii.hexlify(key)) # print the key

    # get plaintext from file
    file = open("./Text Files/Plaintext.txt", "r") 
    plaintext = file.read() 
    file.close()

    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv)) # create the AES object

    encrypted = aes.encrypt(plaintext) # encrypt the plaintext
    hexed = binascii.hexlify(encrypted) # convert the ciphertext to hex
    print("Encrypted Text: ", hexed)
    
    # write the encrypted text to a file
    file = open("./Text Files/Encrypted Text.txt", "wb") 
    file.write(hexed) 
    file.close() 

def decrypt(iv):

    # get encryption key from file
    file = open("./Text Files/Salted Key.txt", "rb") 
    key = file.read() 
    key = binascii.unhexlify(key) 
    file.close() 

    print("Decryption Key: ", binascii.hexlify(key)) # print the key

    file = open("./Text Files/Encrypted Text.txt", "rb") # open the file in read mode
    ciphertext = file.read() # read the file
    file.close() # close the file

    aes2 = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv)) # create the AES object
    
    ciphertext = binascii.unhexlify(ciphertext) # convert the decrypted text to bytes
    decrypted = aes2.decrypt(ciphertext) # decrypt the ciphertext
    print("Decrypted Text: ", decrypted)
    
    # write the decrypted text to a file
    file = open("./Text Files/Decrypted Text.txt", "wb") 
    file.write(decrypted)
    file.close() 
 

if __name__ == '__main__':
    # Make a 256-bit AES encryption key

    key, iv = reduceKey() # reduce the key and get the iv
    while True:
        print('------------------------------------')
        print("Choose An Option: ")
        print("Encryption : E")
        print("Decryption : D") 
        print("Exit : X")
        print('------------------------------------')
        userInput = input("Enter Your Choice: ") # get the user's input
        print('------------------------------------')
        if userInput == 'E': # if the user wants to encrypt
            key, iv = reduceKey() # reduce the key and get the iv
            encrypt(key, iv) # encrypt the plaintext
            
        elif userInput == 'D': # if the user wants to decrypt
            decrypt(iv) # decrypt the ciphertext
        
        elif userInput == 'X': # if the user wants to exit
            print("Exiting Program...")
            break # exit the program