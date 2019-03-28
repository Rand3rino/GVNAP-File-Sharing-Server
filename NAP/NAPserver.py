#figure out list index out of range issue
#multi thread
#add nap functionality

#Python NAP Server
import socket               # Import socket module
import _thread
import pickle
#from multiprocessing import Process # Import multiprocessing module

#stores hostname key to username, port, connection speed
global users, files# = {}
#stores filename key to hostname, file desc
#files = {}

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
#print(host)
#s.bind((host, 2004))        # Bind to the port
s.bind(('localhost', 2121))        # Bind to the port
s.listen(4)

def commandParser(conn, addr,s):
	
	while True:
		command = conn.recv(1024).decode()
		split = command.split()
		print(split)
		#for piece in split:
		#	print(piece)
		if split[0] == "CONNECT":
			# Send to client the number of data rows
			#conn.send(str(1).encode())
			#conn.send(b'User indexed in users table')
			users[addr[0]] = [split[3], str(addr[0]), str(addr[1]), split[4]]
			print("User indexed in users table")
			print(users[addr[0]])
			
		#make multi word desc work
		elif split[0] == "UPLOAD":
			files[split[1]] = [addr[0], str(addr[1]), split[2]]
			print("File indexed in files table")
			print(files[split[1]])
			message = "File indexed in Files table"
			conn.send(message.encode())

		elif split[0] == "SEARCH":

			print(split[1])
			if split[1] in files:
				# Send to client the number of data rows
				# conn.send(str(1).encode())
				print((' '.join(files[split[1]]) + ' ' + ' '.join(users[files[split[1]][0]])))
				conn.send((' '.join(files[split[1]]) + ' ' + ' '.join(users[files[split[1]][0]])).encode())
			else:
				message = "No Matching Records"
				conn.send(message.encode())
		elif split[0] == "TABLES":
			
			# Send to client the number of data rows
			#num = len(users) + 1#len(files) + 2
			#conn.send(str(num).encode())

			# Send the users table
			#conn.send(b'Users\n')
			message = "Users\n"
			for k in users:
				print("Key: ",k)
				print("Value: ", users[k])
				#user = ' '.join(users[k])
				message = message + ' '.join(users[k])
			
			message = message + "\nFiles\n"
			# Send the files table
			#conn.send(b'Files')
			for k in files:				
				print("Key: ",k)
				print("Value: ", files[k])
				message = message + ' '.join(files[k])
			#	files = ' '.join(files[k])
			#	conn.send(files.encode())
			conn.send(message.encode())

		elif split[0] == "LOGOUT": #QUIT

			# Send to client the number of data rows
			message = "Files deleted from files table\nUser deleted from users table"
			conn.send(message.encode())

			#delete info from tables
			for file in files:
				if users[addr[0]][0] == file[0]:
					del file
			#print("Files deleted from files table")
			del users[addr[0]]
			#print("User deleted from users table")
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
			#print("Bad command")
			conn.close()
			break
	print("Quit connection with:", addr)


while True:
	print("Waiting for connection...")
	conn, addr = s.accept()
	print("Got connection from:", addr)	
	_thread.start_new_thread(commandParser, (conn, addr,s))
#	P = Process(target=commandParser, args=(conn, addr)); # jump to function
#	P.start(); # start process
#	P.join();  # join process to server
s.close