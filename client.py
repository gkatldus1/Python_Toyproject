# TCP client example
import socket
import json

def sends():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("172.16.100.74", 5000))

    while True:
        #데이터 딕셔너리로 변환
        balls_info = { "balls_data" : balls }
        weapons_info = { "weapons_data" : weapons}
        character_info = { "character_data" : character_dic}
        #데이터 json으로 변환
        converted_balls_info = json.dumps(ball_info)
        converted_weapons_info = json.dumps(weapons_info)
        converted_character_info = json.dumps(character_info)
        # 서버로 데이터 전송
        client_socket.send(converted_balls_info.encode())
        client_socket.send(converted_weapons_info.encode())
        client_socket.send(converted_character_info.encode())

def receives():
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("172.16.100.74", 5000))
        # 서버로부터 데이터 받기
        received_data = client_socket.recv(1024)
        
        # json을 파이썬 데이터형으로 변환
        converted_python_type_data = json.loads(received_data)
        
        # balls, weapons, character 분류하기
        if "balls_data" in converted_python_type_data:
            another_user_balls = converted_python_type_data["balls_data"]
        elif "weapons_data" in converted_python_type_data:
            another_user_weapons = converted_python_type_data["weapons_data"]
        elif "character_data" in converted_python_type_data["character_data"]:
            another_user_character = converted_python_type_data["character_data"]


