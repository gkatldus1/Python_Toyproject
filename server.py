# TCP server example
import socket
import threading

def echo_thread(client_socket, address):
	print ("I got a connection from ", address)
	while True:
		data = client_socket.recv(512).decode()
		if(data == 'q' or data == 'Q'):
			client_socket.close()
			break;
		else:
			print ("RECEIVED:" , data)
			client_socket.send(data.encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen(5)

clients = []

print ("TCPServer Start")
print("host name : " + server_socket.getsockname()[0])

while True:
	t = threading.Thread(target=echo_thread, args=server_socket.accept())
	t.start()

	clients.append(t)

server_socket.close()
print("SOCKET closed... END")

