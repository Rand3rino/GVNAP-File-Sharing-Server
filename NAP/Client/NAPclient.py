# Python FTP Client
import socket 

while True:
	command = input("Input a command: ")
	split = command.split()
	#debug
	for s in split:
		print(s)
	if split[0] == "CONNECT":
		sock = socket.socket()
		sock.connect((split[1], int(split[2])))
		print("Connected")
	if split[0] == "STORE":
		sock.send(command.encode())
		with open(split[1], 'rb') as f:
			sock.sendfile(f, 0)
		#f = open(split[1],'rb')
		#l = f.read(1024)
		#while (l):
		#	print("Sending...")
		#	sock.sendall(l)
		#	l = f.read(1024)
		#f.close()
		print("Done Sending")
		#sock.shutdown(socket.SHUT_WR)
	if split[0] == "RETRIEVE":
		sock.send(command.encode())
		f = open(split[1],'wb')
		l = sock.recv(1024)
		while (l):
			print("Receiving...")
			f.write(l)
			l = sock.recv(1024)
		f.close()
		print("Done Receiving")
	if split[0] == "QUIT":
		sock.send(command.encode())
		sock.close()
		break