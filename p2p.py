import socket, select, time

s = socket.socket()
s.bind(("10.48.72.71", 8080))
s.listen(10)

connections = [s]

while True:
    time.sleep(.1)

    recv,write,err = select.select(connections,connections,connections)

    for socket in recv:
        if socket == s:
            client,address = socket.accept()
            connections.append(client)
        else:
            msg = socket.recv(4096).decode("UTF-8")
            print("Recieved message from a socket, message was: "+str(msg))

    for socket in write:
        socket.send(bytes("Hi", "UTF-8"))

    for socket in err:
        print("Error with a socket")
        socket.close()
        connections.remove(socket)
