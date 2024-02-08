import socket
import threading
import time
client = socket.socket()
try:
    client.connect(("192.168.100.9",4004))
except :
    raise Exception("Error: server is down")
# else: connected = True


def recv_broadcast(client=client,quit=False):
    while True:
        try:    
            response = client.recv(1024).decode()
        except:
            break
        else:
            print(response)
        # if quit:
        #     print("qiut")
        #     break

def send(): 
    print(client.recv(1024).decode()) # gets you are joined confirmation
    connected = True
    while connected:
        message = input("Message: ")
        client.send(message.encode())
        time.sleep(0.01)
        if message == "quit":
            # print("after recv")
            # recv_broadcast(quit=True)
            client.close()  
            connected = False


if __name__ == '__main__':
        send_thread = threading.Thread(target=send)
        send_thread.start()
        recv_thread=threading.Thread(target=recv_broadcast)
        recv_thread.start()
        # atexit.register(sendmsg("quit"))