import socket
name = socket.gethostname()
print(name)

name2 = socket.gethostbyname('homepage.sch.ac.kr')
print(name2)

name3 = socket.gethostbyname('www.google.com')
print(name3)

name4 = socket.getfqdn('www.google.com')
print(name4)