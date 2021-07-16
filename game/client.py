from socket import *

ip = "14.39.87.152"
port = 5000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip, port))

print("연결 확인됐습니다.")
clientSocket.send("I am a Client".encode("utf-8"))

clientSocket.close



