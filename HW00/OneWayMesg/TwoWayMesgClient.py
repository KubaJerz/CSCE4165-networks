from socket import *

# Import argv related methods
from sys import *


# Client needs server's contact information
if len(argv) != 4:
    print('usage:', argv[0], '<serverName> <port> <clientName>')
    exit()

serverName = argv[1]
serverPort = int(argv[2])
clientName = argv[3]


# Create a socket
sock = socket(AF_INET, SOCK_STREAM)

# Connect to the server
sock.connect((serverName, serverPort))
print(f"Connected to server at ('{serverName}', '{serverPort}')");

# Make a file stream out of socket
sockFile = sock.makefile(mode='rw')

# Keep reading lines and send to server
while True:
    # Send the line to server
    mess = stdin.readline()
    # print(mess)
    mess = f'{clientName}: {mess}'

    sockFile.write(mess)
    sockFile.flush()
    response = f'{sockFile.readline().strip()}'
    print(f'{response}') 

# done
print("Closing connection")
sock.close()