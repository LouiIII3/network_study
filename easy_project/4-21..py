import binascii
import socket
import sys
for string_address in ['114.71.220.95']:
    packed = socket.inet_aton(string_address)
    print ('Original:', string_address)
    print ('Packed :', binascii.hexlify(packed))
    print ('Unpacked:', socket.inet_ntoa(packed))
