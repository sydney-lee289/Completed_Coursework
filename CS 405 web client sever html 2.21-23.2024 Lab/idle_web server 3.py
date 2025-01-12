from socket import*

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', 12000))

server_socket.listen(1)

while True:
    accept_socket, address = server_socket.accept()
    message = accept_socket.recv(2048)
    #print(message.decode())

    first_line = message.decode().split("\n")[0]
    words = first_line.split(" ")
    print(words)

    if words[0] == "GET":
        file_name = words[1][1:]
        f_in = open(file_name)
        file_contents = f_in.read()
        f_in.close()

        #next four lines for header
        accept_socket.send("""HTTP/1.1 200 Document Follows\r\n""".encode())
        content_length_str = "Content-Length:" + str(len(file_contents)) + "\r\n"
        accept_socket.send(content_length_str.encode())
        accept_socket.send("\r\n".encode())
        accept_socket.send(filen_contents.encode())
        
    accept_socket.close()
server_socket.close()
