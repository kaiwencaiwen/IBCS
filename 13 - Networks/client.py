import socket 
import datetime
import time

host="192.168.100.87"
port=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
	my_socket.connect((host, port))
	while True:
		currentDT = str.encode(str(datetime.datetime.now().strftime("%I:%M:%S %p")))
		my_socket.sendall(b'\n\nHi, the time now is ')
		my_socket.sendall(currentDT)
		time.sleep(1)