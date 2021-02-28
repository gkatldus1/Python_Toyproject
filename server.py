# TCP server example
import socket
import threading
import time

class Server:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.soc.bind((self.ip, self.port))
		self.soc.listen(2)
		self.clients = []
		self.loop = True

	def start(self):
		while self.loop:
			client_sock, addr = self.soc.accept()
			self.clients.append(client_sock)
			t = threading.Thread(target=self.echo_thread, args=(client_sock, addr))
			t.start()
		
		self.soc.close()


	def echo_thread(self, client_socket, address):
		print ("new connection : " + str(address[0]))

		print(str(address[0]) + "//wating for other clients...")
		while len(self.clients) < 2 and self.loop:
			time.sleep(1000)

		print(str(address[0]) + "//all clients connected")
		if self.clients[0] == client_socket:
			rival_sock = self.clients[1]
		else:
			rival_sock = self.clients[0]

		while self.loop:
			data = client_socket.recv(512).decode()
			print(str(address[0]) + "//client disconnected")
			if(data == 'q' or data == 'Q'):
				client_socket.close()
				break
			else:
				print (str(address[0]) + "//RECEIVED:" , data)
				rival_sock.send(data.encode())

serv = Server("", 5000)
serv.start();
serv.start();
