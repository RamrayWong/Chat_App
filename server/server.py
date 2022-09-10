from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import E
import time
from user import User


# GLOBAL CONTSTANTS 
HOST = "localhost"
PORT = 6000
BUFSIZ = 1024
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10

# GLOBAL VARS
users = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR) # set up server


def broadcast(msg, name):
    """

    send new messages to all clients
    :param msg: bytes()
    :param name: str
    :return
    """
    for user in users:
        client = user.client
        client.send(bytes(name, "utf-8") + msg)


def client_communication(user):
    """

    Thread to handle all messages from client 
    :param client: socket
    :return:
    """
    run = True
    client = user.client

    # get users name
    name = client.recv(BUFSIZ).decode("utf-8")
    user.set_name(name)
    msg = bytes(f"{name} has joined the chat!", "utf-8")
    broadcast(msg,"") # broadcast welcome message


    while True:
        try:
            msg = client.recv(BUFSIZ)

            if msg == bytes("{quit}", "utf-8"):
                client.close()
                users.remove(user)
                broadcast(bytes(f"{name} has left the chat...", "utf8"), "")
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else: 
                broadcast(msg, name + ": ") 
                print(f"{name}: ", msg.decode("utf-8"))

        except Exception as e:
            print("[EXCEPTION]", e)
            break

def wait_for_connection(SERVER):
    """

    Wait for connection from new clients, start new thread once connected
    :param SERVER: SOCKET
    :return: None

    """

    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            user = User(addr, client)
            users.append(user)
            print(f"[CONNECTION] {addr} connected to server at {time.time()}")
            Thread(target = client_communication, args = (user,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            run = False

    print("SERVER CRASHED")




if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) # listen for connections
    print("Waiting for connections...")
    ACCEPT_THREAD = Thread(target = wait_for_connection, args=(SERVER,)) # Comma because pass tuple
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()