import socket

host = input("shuru:")
ip = socket.gethostbyname(host)
print(ip)