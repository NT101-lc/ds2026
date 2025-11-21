import socket 
PORT = 8080
HOST = '0.0.0.0'

# tranh viec ghi de header
def recv_exact(conn, size):
    data = b""
    while len(data) < size:
        packet = conn.recv(size - len(data))
        if not packet:
            raise ConnectionError("Closed connection")
        data += packet
    return data

s = socket.socket()
s.bind((HOST,PORT))
s.listen(1)
print(f"Server listening on port : {PORT}")

conn, addr = s.accept()
print('Connect by', addr)

name_size = int.from_bytes(recv_exact(conn,4), 'big')

filename = conn.recv(name_size).decode()
print(f"Received file {filename}")


with open('received_' + filename, 'wb') as f:
    while True:
        chunk = conn.recv(1024)
        if not chunk:
            break
        f.write(chunk)

print(f"File {filename} received: OK")
s.close()
