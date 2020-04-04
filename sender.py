#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

s = socket.socket()
host = socket.gethostname()
port = 21
s.bind((host, port))
s.listen(1)
print("Your hostname: "+ host)
print("Waiting for any incomming connections ... ")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input(str( "Please enter the filename of the file: \n" ))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted succesfully ... ")


