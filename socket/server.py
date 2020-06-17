
# importing the socket and datagram modules
from socket import socket, AF_INET, SOCK_DGRAM

# creation of socket module
s = socket(AF_INET, SOCK_DGRAM)
# binding it to the local host
s.bind(('127.0.0.1', 8888))

# Keeps the server in listening mode forever
while True:

    print('Waiting for the client')
    # saves the command and address from which request is received
    command_, addr = s.recvfrom(1024)
    data='No Such Command'

    # decodes the command
    command=command_.decode()

    # executes if the command is a GET command
    if command[:3].upper() == 'GET':

        try:
            # Executes if a file name is present in the GET command
            if command[3:] != '':
                print('Client has requested for', command[4:])

            # tries to open and read the contents of the file
            f = open(command[4:], "r")

            data1=[]
            print('The file contains:')
            data1.append('The file contains:')

            # stores the data into list if there are multiple lines
            for line in f.readlines():

                print(line)
                data1.append(line)


            print('Sending the contents of',command[4:],'to the requested client')

            # converts the data or the list into string in order to send the data to the client as a response.
            data=str(data1)

        except:
            # executes if file name given in the command is not present
            if command[3:] !='':
                data = 'Error:File not found!!!'
                print(data)
            else:
                data = 'Please provide the file name when using get'
                print('No input for text file from the user!!!')


    # executes if the client gives a BOUNCE command
    elif command[:6].upper() == 'BOUNCE':


        if command[7:] != '':
            print('Message from the Client is \'',command[7:],'\'')

        else:
            print('Received Blank message from client')

        # sends the client an echo of the text message sent by the client
        data = 'echo:' + command[7:]

    # Executes if the client gives an EXIT command
    elif command[:4].upper() == 'EXIT':

        # if no exit code is given
        if len(command)==4:
            data='Normal exit from server'
            print('Client took normal exit from server')

        # if an exit code is given by the user
        else:
            print('Client exited due to',command[5:])
            data='Exit due to '+command[5:]

    # executes if the user gives any other command other than these three
    else:
        print('Client requested invalid command')



    print('\n')

    # Encodes and sends the data to the client which has given the command
    s.sendto(data.encode(), addr)
