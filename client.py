from socket import *
import json
import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-p port 7777', action="store", default=False)
parser.add_argument('-a adress localhost', action="store")
print(parser.parse_args())

    

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('localhost', 7777))
    msg = {'action': 'authenticate', 'user': {'account_name': 'test', 'password': 'test'}}
    msg_str = json.dumps(msg)
    s.send(msg_str.encode('utf-8'))
    data = s.recv(1000000)
    print('Сообщение от сервера:', data.decode('utf-8'), ', длинной', len(data), 'байт')
    s.close()
