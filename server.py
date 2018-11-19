import json
from socket import *
from typing import Any, Dict


def handle_authenticate(request):
        if request['user'] == {'account_name': 'test', 'password': 'test'}:
            return{'response': 200}
        return{'response': 402, 'error': 'wrong password'}


mapping = {
    'authenticate': handle_authenticate
}


def handler(request: Dict[str, object]):
    print(f' Client sent {request}')
    response = mapping[request['action']](request)
    print(f' Response: {response}')
    return response


with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(('', 7777))
    s.listen(5)
    while True:
        client, addr = s.accept()
        with client:
            data_b = client.recv(1000000)
            data = json.loads(data_b, encoding='utf-8')
            response = handler(data)
            client.send(json.dumps(response).encode('utf-8'))
