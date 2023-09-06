import socket
import sys

import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully")

except socket.error as err:
    print(f"socket failed {err}")

port = 80

try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror:
    print('error resolving')
    sys.exit()
s.connect((host_ip, port))
print(f'socket has successfully connected on port == {host_ip} ')

# ip = socket.gethostbyname('www.github.com')
# print(ip)
