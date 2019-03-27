#figure out list index out of range issue
#multi thread
#add nap functionality

#Python FTP Server
import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
#print(host)
#s.bind((host, 2004))        # Bind to the port
s.bind(('localhost', 2121))        # Bind to the port
s.listen(4)

while True:
	print("Waiting for connection...")
	conn, addr = s.accept()
	print("Got connection from:", addr)
	while True:
		command = conn.recv(1024).decode()
		split = command.split()

		if split[0] == "STORE":
			with open(split[1],'wb') as f:
				print("Storing...")
				f = open(split[1],'wb')
				l = conn.recv(1024)
				while (len(l)==1024):
					print(len(l))
					f.write(l)
					l = conn.recv(1024)
				f.write(l)
				f.close()
				print("Done Storing")
		elif split[0] == "RETRIEVE":
			print("Sending...")
			with open(split[1], 'rb') as f:
				conn.sendfile(f, 0)
			print("Done Sending")
		elif split[0] == "QUIT":
			conn.close()
			break
		#invalid command
		else:
			print("Bad command")
			conn.close()
			break
	print("Quit connection with:", addr)