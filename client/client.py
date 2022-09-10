from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock

class Client:
    """
    for communication with server
    """
    HOST = "localhost"
    PORT = 6000
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    def __init__(self, name):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        receive_thread = Thread(target = self.receive_messages)
        receive_thread.start()
        self.send_message(name)
        self.lock = Lock()

    def receive_messages(self):
        """
        Init object and send name to server
        :return: None
        """


        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode("utf8")
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("[EXCEPTION]", e)
                break

    def send_message(self, msg):
        """
        send messages to server
        :param msg: str
        :return: None
        """
        self.client_socket.send(bytes(msg, "utf-8"))
        if msg == "{quit}":
            self.client_socket.close()

    def get_message(self):
        """
        :returns a list of str messages
        :return: list[str]
        """
        self.lock.acquire()
        self.lock.release()
        return self.messages

    def disconnect(self):
        self.send_message("{quit}")