import socket
import cryptASCII
import cryptSettings
import sys
import select

# Settings imports (Look at cryptSettings.py for more info)
host = cryptSettings.hostServer()
socketList = []
recvBuffer = cryptSettings.recvBuffer()
port = int(cryptSettings.port())
dis = cryptSettings.displacement()

def reciever():
    net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    net.bind((host, port))
    net.listen(10)
    socketList.append(net)
    # To tell you when a client connects
    print "Chat server started on port " + str(port)
 
    while 1:       
        ready_to_read,ready_to_write,in_error = select.select(socketList,[],[],0)
        for sock in ready_to_read:
            if sock == net: 
                sockfd, addr = net.accept()
                socketList.append(sockfd)
                print "Client (%s, %s) connected" % addr
            else:
                try:
                    data = sock.recv(recvBuffer)
                    if data:
                        decryptText = cryptASCII.decrypt(data, dis)
                        print decryptText
                    else:    
                        if sock in socketList:
                            socketList.remove(sock)
                        broadcast(net, sock, "Client (%s, %s) is offline\n" % addr) 
                except:
                    continue

    net.close()
# Broadcast function isn't truely needed (it's leftover from when the reciever was a server for a chatroom program),
# however it is needed for if the client disconnects it can still reconnect since the server is still left running
# (If the socketList wasn't here the server would close every time a client disconnects)
def broadcast (net, sock, message):
    for socket in socketList:
        if socket != net and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                if socket in socketList:
                    socketList.remove(socket)
 
if __name__ == "__main__":

    sys.exit(reciever())

         



