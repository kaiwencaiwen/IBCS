import socket 
host="192.168.102.125"
port=65432

my_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((host,port))

maintain_connection = True
while maintain_connection:
	my_socket.listen()
	connection, address = my_socket.accept()
	while True:
		data=connection.recv(1024)
		data= data.decode('utf-8')
		if not data:
			break
		print(str(address[0])+": "+data)
	#print(connection,address)
	maintain_connection=False

my_socket.close()