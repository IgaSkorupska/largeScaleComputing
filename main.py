# -*- coding: utf-8 -*-
import socket
import json
from _thread import *

import requests

# a function that handles requests from the individual client by a thread
#threaded_client() connects to each individual client on the different address given by the server
def threaded_client(connection):
    welcome = 'Welcome to the Server\n'
    connection.send(str.encode(welcome))
    
    #registration
    try:
        idx = connection.recv(1024).decode('utf-8')
        name = connection.recv(1024).decode('utf-8')
    except:
        response = 'Registration error: incorrect format'
        connection.send(str.encode(response))
        connection.close()
    
    if idx == '5856e6cd-0da6-4573-9a04-cbb11f5e68d3' and name == 'KÃ¼ppers, Bastian':
        response = 'Registration successful'
        connection.send(str.encode(response))
    else:
        response = 'Registration error: incorrect credentials'
        connection.send(str.encode(response))
        connection.close()
        
    while True:
        message = connection.recv(1024).decode('utf-8')
        print('Received message:' + message)
        reply = ('Thank you for sending us a message! If we could, we would pass it on to another user!')
        connection.send(str.encode(reply))
        

    connection.close()

def server():
    ServerSocket = socket.socket()
    # declare host and port on which we need to communicate with clients
    ip = "127.0.0.1"
    print(ip)
    port = 13370
    ThreadCount = 0
    #if it binds successfully then it starts waiting for the client otherwise
    # it returns the error that occurred while establishing a connection
    try:
        ServerSocket.bind((ip, port))
    except socket.error as e:
        print(str(e))
    print('Waitiing for a Connection..')
    ServerSocket.listen(5)
    # use a while loop to make it run Server endlessly until we manually stop the Server
    while True:
        # accept connection from client using accept() function of socket server.
        # It returns the type of client which has connected and along with the unique thread number or address provided to it.
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        # Registration(id, firstname, publickey, ServerSocket, client1)
        # use start_new_thread() function of thread class which creates or assign a new thread to each client to handle them individually.
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
      # ThreadCount == 1:
            #change the path according to location of config_1.json in your laptop

       # if ThreadCount == 2:

    ServerSocket.close()

#def Registration(id, firstname,  publickey, s,client1):

if __name__ == '__main__':
    server()
