import socket
import threading
import json
import ECDH_IMP
import AES
import base64
def handle_client(client_socket):

        #key exchange part
        data = client_socket.recv(1024).decode('utf-8')
        deserializedData=json.loads(data)
        AlicePublicKey=deserializedData['AlicePublicKey']
        print()
        print("Alice Public Key:")
        print()
        print(AlicePublicKey)
        BobPublicKey=ECDH_IMP.calculatePublicKey(128)
        data_to_send = {
            'BobPublicKey': BobPublicKey
        }
        client_socket.send(json.dumps(data_to_send).encode('utf-8'))
        sharedKey=ECDH_IMP.calculateSharedKey(AlicePublicKey)
        print()
        print("Here is the shared key:")
        print(sharedKey)
        print()
        #receiving iv
        data=client_socket.recv(1024)
        iv=base64.b64decode(data)
        print("Initialization vector:")
        print(iv)
        print()
        #decryption part
        data=client_socket.recv(1024)
        receivedCipherText=base64.b64decode(data)

        print("Received Cipher text from Alice:")
        print(receivedCipherText)
        print()

        roundKeys=AES.key_scheduling(sharedKey)
        mainMessage=AES.AES_Decryption(bytearray(receivedCipherText),roundKeys,iv)

        print("Decrypted Final Message:")
        plain = ("".join(map(chr, mainMessage))).rstrip(chr(4))
        print(plain, end=" [IN ASCII]\n\n")
        print()
        #print(f"Received from client: {data}")
        #response = input("Enter your response: ")
        #client_socket.send(response.encode('utf-8'))
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))  # Change the IP and port if needed
    server.listen(5)
    print("Server listening on port 12345...")

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
