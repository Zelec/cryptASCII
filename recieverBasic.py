import socket
import cryptASCII
import cryptSettings
import sys
import select

host = cryptSettings.hostServer()
socketList = []
recvBuffer = cryptSettings.recvBuffer()
port = int(cryptSettings.port())
dis = cryptSettings.displacement()

def reciever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(10)
    socketList.append(s)

    print "Chat server started on port " + str(port)
 
    while 1:       
        ready_to_read,ready_to_write,in_error = select.select(socketList,[],[],0)
        for sock in ready_to_read:
            if sock == s: 
                sockfd, addr = s.accept()
                socketList.append(sockfd)
                print "Client (%s, %s) connected" % addr
            else:
                try:
                    data = sock.recv(recvBuffer)
                    if data:
						#decryptText = cryptASCII.decrypt(data, dis)
						print data
                    else:    
                        if sock in socketList:
                            socketList.remove(sock)
                        broadcast(s, sock, "Client (%s, %s) is offline\n" % addr) 
                except:
                    continue

    s.close()
    
def broadcast (s, sock, message):
    for socket in socketList:
        if socket != s and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                if socket in socketList:
                    socketList.remove(socket)
 
if __name__ == "__main__":

    sys.exit(reciever())

         



