import socket
HOSTS = [
'www.sch.ac.kr',
'homepage.sch.ac.kr',
'www.daum.net',
'www.google.com',
'iot',
'lsporoject.shop'
]
for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))