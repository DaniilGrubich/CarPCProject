import socket
import time 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8585 ))
s.listen(0)                 

while True:
    client, addr = s.accept()
    client.settimeout(5)
    while True:
        try:
            content = client.recv(1024)
        except:
            break

        if len(content) ==0:
           break
        else:
            print(str(content,'utf-8'))
            client.send(b'@KXZF0$')
    client.close()
