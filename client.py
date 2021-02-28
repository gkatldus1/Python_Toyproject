# TCP client example
import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값

# 공들
balls = {'user':{'name':'siyeon'}}

while True:
    data = input ( "SEND( TYPE q or Q to Quit):" )
    if ( data == 'q' or data == 'Q'):
        client_socket.send(data.encode())
        client_socket.close()
        break;
    if data == 'balls':
        client_socket.send(json.dumps(balls).encode())
print ("socket colsed... END.")