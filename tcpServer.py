#!/bin/python

import socket

BUFFER = 4096  #buffer size for data 
TCPPORT = 9999

def tcpServer():
   srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   srvsock.bind(('', TCPPORT))
   srvsock.listen(5)

   while True:
      clisock, (remoteHost, remotePort) = srvsock.accept()
      print("[%s:%s] connected..." % (remoteHost, remotePort))
   
      while True:
         dat = clisock.recv(BUFFER)
         if not dat:
            clisock.close()
            break
         print("[Client %s:%s said:] %s " % (remoteHost,remotePort,dat))
         clisock.send(b'server has received your message...')
         #break
      #break
   
   clisock.close()
if __name__ == '__main__':
   tcpServer()



