from ctypes.wintypes import CHAR
import socket
from dataclasses import dataclass
import numpy as np
import pickle
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

questionArray = []
#----------------------------------------------------------------------------
q1 = question(1, 'What is the capital  of Egypt?', 'Alexandria', 'Mansoura', 'Paris','Cairo','Cairo')
q2 = question(2, 'How many blue stripes in the US flag?', '6', '7', '13','0','13')
q3 = question(3, 'Bob parents ...... are not sure where his sister is?', 'herself', 'himself', 'ourselves','themselves','themselves')
q4 = question(4, 'Which of the following is connection oriented protocol?', 'TCP', 'SMTP', 'FTP', 'UDP', 'TCP')
q5 = question(5, 'What is the port number of http?', '50', '25', '80', '24', '80')
q6 = question(6, 'What is the protocol responsible for mail transfer?', 'SMTP', 'FTP', 'HTTP', 'IP', 'SMTP')
q7 = question(7, 'What is the port number of SMTP?', '50', '25', '80', '24', '25')
q8 = question(8, 'What is the layer responsible for packet forwarding including routing through intermediate routers?', 'Session', 'Network', 'Transport', 'Data link', 'Network')
q9 = question(9, 'How many layer are there in the OSI model?', '4', '5', '6', '7', '7')
q10 = question(10, 'Transport layer aggregates data from different applications into a single stream before passing it to', 'Network layer', 'Data link layer', 'Appliction layer', 'Physical layer', 'Network layer')

questionArray.append(q1)
questionArray.append(q2)
questionArray.append(q3)
questionArray.append(q4)
questionArray.append(q5)
questionArray.append(q6)
questionArray.append(q7)
questionArray.append(q8)
questionArray.append(q9)
questionArray.append(q10)
#----------------------------------------------------------------------------

serverPort = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = ('127.0.0.1', serverPort)
server.bind(ADDR)
server.listen(5)
print('The server is ready to send')

while 1:
    connectionSocket, addr = server.accept()
    connectionSocket.send(bytes("Thank you for connecting...", "utf-8"))

    rnd = np.random.permutation(11)[:5]

    for i in range(5):
        dataString = pickle.dumps(questionArray[rnd[i]])
        connectionSocket.send(dataString)
        time.sleep(0.2)

    connectionSocket.close()
    break
