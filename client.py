# TCP client example
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))
while True:
    data = input ( "SEND( TYPE q or Q to Quit):" )
    if ( data == 'q' or data == 'Q'):
        client_socket.send(data.encode())
        client_socket.close()
        break;
    else:
        client_socket.send(data.encode())
print ("socket colsed... END.")