import pickle
import socket
from dataclasses import dataclass
import time

@dataclass
class question:
    num: int
    Q: str
    a: str
    b: str
    c: str
    d: str
    ans: str



s = socket.socket()

port = 12000

s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())

for i in range(5):

    data = s.recv(4096)
    dataVariable = pickle.loads(data)
    print('Q' + str(i+1) + '- ' + dataVariable.Q)
    print('a- ' + dataVariable.a)
    print('b- ' + dataVariable.b)
    print('c- ' + dataVariable.c)
    print('d- ' + dataVariable.d)
    print(' ')
    time.sleep(0.2)

s.close()