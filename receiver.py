#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket()
host = input(str("Please enter host address of sender: "))
port = 21
s.connect((host, port))
print("Connected ...")

