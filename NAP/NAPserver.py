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
		#for piece in split:
		#	print(piece)
		if split[0] == "STORE":
			with open(split[1],'wb') as f:
				f = open(split[1],'wb')
				#print "Receiving..."
				l = conn.recv(1024)
				while (len(l)==1024):
					print(len(l))
					print("Storing...")
					f.write(l)
					l = conn.recv(1024)
				f.write(l)
				f.close()
				print("Done Storing")
				#conn.shutdown(socket.SHUT_WR)
		elif split[0] == "RETRIEVE":
			f = open(split[1],'rb')
			#print 'Sending...'
			l = f.read(1024)
			while (l):
				print("Sending...")
				conn.send(l)
				l = f.read(1024)
			f.close()
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