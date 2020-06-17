These python scripts were run on Pycharm IDE of python version 3.8.
Whenever the client sends a GET command with a text file, the server prints the contents of the file and returns the contents of the file requested in the GET command.
Whenever the client sends a BOUNCE command with a text, The server prints this text message and sends an echo to the client which is the same text.

When client sends Exit command:
The server checks if there is any exit code sent from the client.
If no exit code, the server prints it as 'Client took normal exit from server', and sends a message 'Normal exit from server' to the client.
If there is any exit code in the command, The server prints the code due to which the client exited.

Syntax of the commands:
Please use the same syntax as below:
GET_filename.txt
GET_info.txt
BOUNCE_textmessage
EXIT_exitcode