#figure out list index out of range issue
#multi thread
#add nap functionality

#Python NAP Server
import socket               # Import socket module

#stores hostname key to username, port, connection speed
users = {}
#stores filename key to hostname, file desc
files = {}

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
		if split[0] == "CONNECT":
			users[addr[0]] = [split[3], str(addr[1]), split[4]]
			print("User indexed in users table")
		#make multi word desc work
		elif split[0] == "UPLOAD":
			files[split[1]] = [addr[0], split[2]]
			print("File indexed in files table")
		elif split[0] == "SEARCH":
			if split[1] in files:
				#result = 
				conn.send((' '.join(files[split[1]]) + ' ' + ' '.join(users[files[split[1]][0]])).encode())
		elif split[0] == "TABLES":
			print("Users")
			for k in users:
				print("Key: ",k)
				print("Value: ", users[k])
			print("Files")
			for k in files:
				print("Key: ",k)
				print("Value: ", files[k])
		elif split[0] == "QUIT":
			#delete info from tables
			for file in files:
				if users[addr[0]][0] == file[0]:
					del file
			print("Files deleted from files table")
			del users[addr[0]]
			print("User deleted from users table")
			conn.close()
			break
		elif split[0] == "STOP":
			exit()
		#invalid command
		else:
			print("Bad command")
			conn.close()
			break
	print("Quit connection with:", addr)
