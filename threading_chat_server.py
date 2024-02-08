import socket
import threading
clients = []
def broadcast(message):
    for client in clients:
            print("broadcasted")
            client.send(message.encode())

def handle_connection(client:socket.socket,clientport):
    clients.append(client)
    broadcast(f'a user from {clientport[1]} has joined')
    client.send("you have joined".encode())
    connected = True
    while connected:
        print("waiting for message")
        message = client.recv(1024).decode()
        if message == "quit":
            broadcast(f"User {clientport[1]} has disconnected")
            clients.remove(client)
            connected = False
        else:    
            broadcast((f"user id {clientport[1]} says: {message}"))
    
# print(socket.gethostname())
if __name__ == '__main__':
    server = socket.socket()
    server.bind(("192.168.100.9", 4004))
    server.listen()
    print("server is running")
    while True:
        clientaddr , clientport  = server.accept()
        handle_thread=threading.Thread(target=handle_connection,kwargs={"client":clientaddr,"clientport":clientport} )
        print(f"no of connections is {threading.active_count()}")
        handle_thread.start()
