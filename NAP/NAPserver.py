#figure out list index out of range issue
#multi thread
#add nap functionality

#Python NAP Server
import socket               # Import socket module
import _thread				# Import thread module

#from multiprocessing import Process # Import multiprocessing module

#stores hostname key to username, port, connection speed
users = {}
#stores filename key to hostname, file desc
files = {}

s = socket.socket()         # Create a socket object
s.bind(('localhost', 2121))        # Bind to the port
s.listen(4)

def commandParser(conn, addr,s):
	
	while True:
		command = conn.recv(1024).decode()
		split = command.split()
		print(split)

		if split[0] == "CONNECT":
			users[addr[1]] = [split[3], str(addr[0]), str(addr[1]), split[4], split[5]]
			print("User indexed in users table")
			print(users[addr[1]])
			
		#make multi word desc work
		elif split[0] == "UPLOAD":

			# Store IP, Port Num, File Name, File Description, Ftpserver port
			files[split[2]] = [addr[0], str(addr[1]), split[1], split[2], split[3]]
			print("File indexed in files table")
			print(files[split[2]])
			message = "File indexed in Files table"
			conn.send(message.encode())

		elif split[0] == "SEARCH":
			if split[1] in files:
				message = ' '.join(files[split[1]])
				conn.send(message.encode())
			else:
				message = "No Matching Records"
				conn.send(message.encode())
		elif split[0] == "TABLES":
			
			# Send the users table
			message = "Users\n"
			for k in users:
				message = message + ' '.join(users[k]) + "\n"
			
			message = message + "\nFiles\n"
			# Send the files table
			for k in files:				
				message = message + ' '.join(files[k]) + "\n"
			conn.send(message.encode())

		elif split[0] == "LOGOUT": #QUIT

			# Send to client the number of data rows
			message = "Files deleted from files table\nUser deleted from users table"
			conn.send(message.encode())
			#delete info from tables
			for file in list(files):
				#if users[addr[0]][0] == file[0]:
				if users[addr[1]][2] == files[file][1]:
					del files[file]
			del users[addr[1]]
			conn.close()
			break
		elif split[0] == "STOP":
			message = "Server Shutting Down"
			conn.send(message.encode())
			exit()
			#conn.close() or quit()

		#invalid command
		else:
			# Send to client the number of data rows
			message = "Bad Command"
			conn.send(message.encode())
			conn.close()
			break
	print("Quit connection with:", addr)


while True:
	print("Waiting for connection...")
	conn, addr = s.accept()
	print("Got connection from:", addr)	
	_thread.start_new_thread(commandParser, (conn, addr,s))
s.close
