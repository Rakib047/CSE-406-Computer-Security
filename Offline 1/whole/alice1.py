import socket
import AES
import ECDH_IMP
import json
import base64
import os

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))  # Connect to the server's IP and port

    #key exchange part
    AlicePublicKey=ECDH_IMP.calculatePublicKey(128)
    data_to_send = {
        'AlicePublicKey': AlicePublicKey
    }
    client.send(json.dumps(data_to_send).encode('utf-8'))

    #client.send(message.encode('utf-8'))
    # response = client.recv(1024).decode('utf-8')
    # print(f"Received from server: {response}")
    data = client.recv(1024).decode('utf-8')
    deserializedData=json.loads(data)
    BobPublicKey=deserializedData['BobPublicKey']
    print()
    print("Bob's Public key:")
    print(BobPublicKey)
    print()
    sharedKey=ECDH_IMP.calculateSharedKey(BobPublicKey)
    print("Here is the shared key:")
    print(sharedKey)
    print()
    #sending iv
    iv = bytearray(os.urandom(16))
    print("Initialization vector:")
    print(iv)
    print()
    client.send(base64.b64encode(iv))
    #encryption part
    message = input("Enter the message you want encrypt and send: ")
    roundKeys=AES.key_scheduling(sharedKey)
    cipherText=AES.AES_Encryption(message,roundKeys,iv)
    client.send(base64.b64encode(cipherText))
    print()

    print("Main message that will be sent to Bob:")
    print(message)
    print()
    print("Encrypted form of the message sent to Bob:")
    print(cipherText)
    print()

    client.close()

if __name__ == "__main__":
    start_client()
