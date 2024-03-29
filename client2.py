import socket
import threading

from rsa_fun import *

IP = "localhost"
PORT_R=1234
PORT_S=50036

class Client2 (threading.Thread):
    def __init__(self , login , sendTo ):
        self.login = login
        self.sendTo = sendTo
        self.myKey , self.pubKey = getKeys(login, sendTo)
        x1 = threading.Thread(target=self.sending)
        x2 = threading.Thread(target=self.receiving)
        x1.start()
        x2.start()

    def sending(self): # behaves like a client
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect((IP,PORT_S))
        while True :
            print()
            msg = input("Enter the message you want to send:   ")
            encrytMsg = encrypt(msg, self.pubKey)
            s.send(encrytMsg)
            print("message sent")

    def receiving(self): # behaves like a server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((IP,PORT_R))
        while True :
            encrytedMsg = s.recvfrom(PORT_S)
            Msg = decrypt(encrytedMsg[0], self.myKey)
            print()
            print("from ",self.sendTo," :",Msg)
            print()

c= Client2("salma","amira")