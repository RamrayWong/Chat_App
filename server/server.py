from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import E
import time
from user import User


# GLOBAL VARIABLES
HOST = "localhost"
PORT = 6000
BUFSIZ = 1024
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10




def client_communication(user):
    """

    Thread to handle all messages from client 
    :param client: socket
    :return:
    """

        
    run = True
    client = user.client
    addr = user.addr

    # get users name
    name = client.rcv(BUFSIZ).decode("utf8")
    msg

    while run:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            client.close()
        else: pass


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
            user = User(addr, name, client)
            print(f"[CONNECTION] {addr} connected to server at {time.time()}")
            Thread(target = handle_client, args = (user,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False

print("SERVER CRASHED")


SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) # listen for connections
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target = wait_for_connection, args=(SERVER,)) # Comma because pass tuple
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()