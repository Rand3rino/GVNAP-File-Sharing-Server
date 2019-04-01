# Python FTP Client
import socket 
import threading				# Import thread module

def createServer():	
	s = socket.socket()			# Create a socket object
	s.bind(('localhost', serverPort))        # Bind to the port	
	s.listen(4)
	print("Waiting for connection...")

	while True:
		conn, addr = s.accept()
		server = threading.Thread(name='server', target=commandParser, args= (conn,addr,s))
		server.start()
	s.close

	#server	
def commandParser(conn, addr,s):
	while True:	
		command = conn.recv(1024).decode()
		split = command.split()

		if split[0] == "STORE":
			with open(split[1],'wb') as f:
				f = open(split[1],'wb')
				l = conn.recv(1024)
				while (len(l)==1024):
					f.write(l)
					l = conn.recv(1024)
				f.write(l)
				f.close()
		elif split[0] == "CONNECT":
			print("Got connection from:", addr)	
		elif split[0] == "RETRIEVE":
			print("Sending...")
			with open(split[1], 'rb') as f:
				conn.sendfile(f, 0)
		elif split[0] == "QUIT":
			conn.close()
			break
			#invalid command
		else:
			print("Bad command")
			conn.close()
			break
	print("Quit connection with:", addr)

#_thread.start_new_thread(createServer, ())


def client():	
	cs = threading.Thread(name='createServer', target=createServer) 
	cs.start()
	while True:
		#_thread.start_new_thread(createServer, ())
		command = input("Input a command: ")
		command = command + " " + str(serverPort)
		split = command.split()
		print(" ")
		if split[0] == "CONNECT":
			sock = socket.socket()
			sock.connect((split[1], int(split[2])))
			sock.send(command.encode())
			print (command.encode())
		elif split[0] == "STORE":
			sock.send(command.encode())
			with open(split[1], 'rb') as f:
				l = f.read(1024)
				while (l):
					sock.send(l)
					l = f.read(1024)
		elif split[0] == "RETRIEVE":
			sock.send(command.encode())
			with open(split[1],'wb') as f:
					f = open(split[1],'wb')
					l = sock.recv(1024)
					while (len(l)==1024):
						f.write(l)
						l = sock.recv(1024)
					f.write(l)
					f.close()
		elif split[0] == "QUIT":
			sock.send(command.encode())
			sock.close()
			break
		else:
			sock.send(command.encode())
			print(sock.recv(1024).decode())

serverPort = 2004
c = threading.Thread(name='client', target=client)
c.start()