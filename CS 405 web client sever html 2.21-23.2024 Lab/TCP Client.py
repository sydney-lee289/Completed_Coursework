from socket import *
client_socket = socket(AF_INET, SOCK_STREAM)

message = input('Enter message to send: ')

server_name = 'localhost'
server_port = 12500
client_socket.connect((server_name, server_port))
client_socket.send(message.encode())
new_message = client_socket.recv(2048)
print('From server: ' + new_message.decode())

client_socket.close()