import os
import socket
HOST = '127.0.0.1'
PORT = 8080
file = input("Enter file:")
if not os.path.isfile(file):
    print("File not exist")
    exit(1)

s = socket.socket()
s.connect((HOST,PORT))

print('Connected to server!')

# send header size
name_byte = file.encode()
s.send(len(name_byte).to_bytes(4,'big'))
s.send(name_byte)

s.send(file.encode())
with open (file, 'rb') as f:
    while data := f.read(1024):
        s.send(data)

print('file send successfully')
s.close()
