#!/bin/python

import socket

BUFFER = 4096
TCPPORT = 9999

def tcpClient():
   clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   clisock.connect(('localhost',TCPPORT))

   clisock.send(b'hello, tcpServer!')
   dat = clisock.recv(BUFFER)
   print("[tcpServer said:] %s" % dat)

  
   clisock.close()
if __name__ == "__main__":
   tcpClient()
