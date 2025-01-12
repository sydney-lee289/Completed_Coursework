from socket import*

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(("93.184.216.34", 80))
client_socket.send("GET / HTTP/1.1\r\nHost: example.com\r\n".encode())
                   
message = client_socket.recv(2048)
print(message.decode())
