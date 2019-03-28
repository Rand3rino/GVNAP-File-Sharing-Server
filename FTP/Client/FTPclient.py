# Python FTP Client
import socket 

while True:
	command = input("Input a command: ")
	split = command.split()
	print(" ")
	if split[0] == "CONNECT":
		sock = socket.socket()
		sock.connect((split[1], int(split[2])))
		print("Connected")
		
		sock.send(command.encode())
		print (command.encode())
		#print(sock.recv(4096).decode())
		#break
	elif split[0] == "STORE":
		sock.send(command.encode())
		with open(split[1], 'rb') as f:
			sock.sendfile(f, 0)
		print("Done Sending")
	elif split[0] == "RETRIEVE":
		sock.send(command.encode())
		with open(split[1],'wb') as f:
				f = open(split[1],'wb')
				#print "Receiving..."
				l = sock.recv(1024)
				while (len(l)==1024):
					print(len(l))
					print("Storing...")
					f.write(l)
					l = sock.recv(1024)
				f.write(l)
				f.close()
				print("Done Receiving")
	elif split[0] == "QUIT":
		sock.send(command.encode())
		sock.close()
		break
	else:
		sock.send(command.encode())
		#num = (sock.recv(1024).decode())
		#print(num)
		#for i in range(int(num)):
		#	print(i)
		print(sock.recv(1024).decode())

