# TCP client example
import socket
import json
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("172.16.100.74", 5000))

# while True:
# 데이터 json으로 변환
balls = [
    {"num": 1},
    {"num":2},
    {"num":3}
]
ball_info = { "ball_data" : balls }
convert_data = json.dumps(ball_info)

#  ball_info = json.dumps(balls)
# character_info = json.dumps(character)
# weapons_info = json.dumps(weapons)
print(ball_info)
# data = input ( "SEND( TYPE q or Q to Quit):" )
# if ( data == 'q' or data == 'Q'):
#     client_socket.send(data.encode())
#     client_socket.close()
#     break
# # 클라이언트 데이터 보내기
# else:
    # client_socket.send(data.encode())
client_socket.send(convert_data.encode())
print("Success")
    # client_socket.send(character_info.encode())
    # client_socket.send(weapons_info.encode())

# print ("socket colsed... END.")