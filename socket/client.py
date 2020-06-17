
# importing the socket and datagram modules
from socket import socket, AF_INET, SOCK_DGRAM

# creation of socket module
s=socket(AF_INET, SOCK_DGRAM)

# binding it to the local host
s.bind(('127.0.0.1',0))

# Assigning the local host as the server
server=('127.0.0.1',8888)


# Keeps the client running until the client wants to exit
while True:

    # Prompts user to enter the command/request
    str = input("Enter your request:\n")



    # Encodes and sends the command requested by the client to the server
    s.sendto(str.encode(), server)

    # Receives data from the server
    data, addr = s.recvfrom(1024)
    print('Message from server:')
    try:
        # if received data is list
        data = data.decode('utf-8')
        # Convert decoded data into list
        data = eval(data)
        for x in data:
            print(x)

    except:
        # if received data is not a list but a string
        print(data)

    print('\n')

    # executes if the client commands to exit
    if str[:4].upper() == 'EXIT':
        # breaks the while loop
        break
