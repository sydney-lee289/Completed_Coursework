from socket import *
server_socket= socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 12500))
server_socket.listen(1)
print('The server is able to receive data.')

while True:
   connection_socket, address = server_socket.accept()
   print(address)
   message = connection_socket.recv(2048)
   new_message = message.decode().upper()

   connection_socket.send(new_message.encode())
   connection_socket.close