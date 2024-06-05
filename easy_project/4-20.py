import socket
for port in [80, 443, 21, 25, 143, 993, 110, 995]:
    url ='{}://example.co.kr/'.format(socket.getservbyport(port))
    print('{:4d}'.format(port), url)
    
