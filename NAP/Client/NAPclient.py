# Python NAP Client
import socket 

while True:
	command = input("Input a command: ")
	split = command.split()
	#CONNECT ip port uname cspeed
	if split[0] == "CONNECT":
		sock = socket.socket()
		sock.connect((split[1], int(split[2])))
		print("Connected")
		sock.send(command.encode())
	#UPLOAD fname desc
	if split[0] == "UPLOAD":
		sock.send(command.encode())
	#SEARCH fname
	if split[0] == "SEARCH":
		sock.send(command.encode())
		info = sock.recv(1024).decode()
		print(info)
	#TABLES
	if split[0] == "TABLES":
		sock.send(command.encode())
	#QUIT
	if split[0] == "QUIT":
		sock.send(command.encode())
		sock.close()
		break
	if split[0] == "STOP":
		sock.send(command.encode())
	#use elif to error handle
