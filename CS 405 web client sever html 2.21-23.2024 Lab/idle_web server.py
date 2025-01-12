from socket import*

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', 12000))

server_socket.listen(1)

accept_socket, address = server_socket.accept()
message = accept_socket.recv(2048)

print(message.decode())

accept_socket.send("""HTTP/1.1 200 OK\r
Content-Length: 10\r\n\r
Hi there!\r\n"""

accept_socket.close()
server_socket.close()
