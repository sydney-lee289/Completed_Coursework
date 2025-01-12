
from socket import*

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(("localhost", 12000))
client_socket.send("GET /FirstnameLastname.html HTTP/1.1\r\nHost: localhost\r\n".encode())
                   
message = client_socket.recv(2048)
print(message.decode())
