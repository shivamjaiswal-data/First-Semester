import socket

server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for connection...")

conn, addr = server.accept()
print("Connected:", addr)

while True:
    msg = conn.recv(1024).decode()

    if not msg:
        break

    print("Friend:", msg)

    reply = input("You: ")
    conn.send(reply.encode())