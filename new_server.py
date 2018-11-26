import select
import socket
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 7777))
server.listen()

sockets = [server]
message_queues = {}

def close_connection(con):
    sockets.remove(con)
    if con in message_queues:
        del message_queues[con]
    con.close()


# Пока есть хоть один сокет
while sockets:
    
    readable, writable, exceptional = select.select(sockets, sockets, sockets, 1)

    for s in readable: 
        if s is server: 
            connection, client_address = s.accept()
            connection.setblocking(0) 
            sockets.append(connection) 
            message_queues[connection] = queue.Queue() 
        else:
            try:
                data = s.recv(1024) 
            except:
                close_connection(s) 
            else: 
                if data:
                    for c in message_queues: 
                        if c != s: 
                            message_queues[c].put(data) 
                else:
                    
                    close_connection(s)

    for s in writable: 
        try:
            next_msg = message_queues[s].get_nowait() 
        except queue.Empty:
            pass 
        except KeyError:
            pass 
        else:
            s.send(next_msg) 

    for s in exceptional: 
        close_connection(s) 
