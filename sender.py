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


