# TCP server example
import socket
import threading
import time

class Server:
    ##초기화 함수
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.soc.bind((self.ip, self.port))
		self.soc.listen(2)
		self.clients = []
		self.loop = True
		self.accept_loop = True
		self.user_count = 0
		self.count = 0
		self.user_thread = []

	#시작 함수
	def start(self):
		while self.accept_loop:
			client_sock, addr = self.soc.accept()
			self.clients.append(client_sock)

			#각 클라이언트마다 따로 스레드로 송수신
			threading._start_new_thread(self.echo_thread, (client_sock, addr))
			#threading._start_new_thread(self.test, (client_sock, addr))
		
		self.soc.close()

	#상대편에게 보내는 함수
	def echo_thread(self, client_socket, address):
		print ("new connection : " + str(address[0]))

		#클라이언트가 2명이상 들어올때까지 대기
		print(str(address[0]) + "//wating for other clients...")
		while len(self.clients) < 2 and self.loop:
			time.sleep(1)

		# 두명이 다 들어왔으면 클라이언트들에게 준비 하라는 신호를 보냄
		# self.clients[0].send("Get Ready".encode())
		# self.clients[1].send("Get Ready".encode())

		#상대 클라이언트 소켓 파악
		print(str(address[0]) + "//all clients connected")
		if self.clients[0] == client_socket:
			rival_sock = self.clients[1]
		else:
			rival_sock = self.clients[0]

		#데이터를 수신받고, 수신받은 데이터를 바로 상대에게 전송
		print (str(address[0]) + "//Receive start")
		while self.loop:
			try:
				data = None
				data = client_socket.recv(1024).decode()
				print (str(address[0]) + "//Received:" + data)
				if(data == 'q' or data == 'Q'):
					print(str(address[0]) + "//client disconnected")
					self.loop = False
					client_socket.close()
					break
				else:
					rival_sock.send(data.encode())
					print (str(address[0]) + "//Send:" + data)
				time.sleep(1)
			except Exception as e:
				print("unexpected exception when checking if a socket is closed")
				self.loop = False

	#보낸 본인에게 다시 전송
	def test(self, client_socket, address):
		try:
			print ("new connection : " + str(address[0]))
			while self.loop:
				data = client_socket.recv(512).decode()
				print (str(address[0]) + "//Test Received:" + data + "   count:" + str(self.count))
				if(data == 'q' or data == 'Q'):
					print(str(address[0]) + "//client disconnected")
					self.loop = False
					client_socket.close()
					break
				if data == '': # 100번 이상 빈데이터가 들어오면 연결 해제
					self.count += 1
					if self.count >= 100:
						self.loop = False
				else :
					self.count = 0
				print (str(address[0]) + "//Test Send:" + data)
				client_socket.send(data.encode())
			self.loop = True
		except Exception as e:
			print("unexpected exception when checking if a socket is closed") #예외 처리
			self.loop = False
		
serv = Server("", 5000)
serv.start()