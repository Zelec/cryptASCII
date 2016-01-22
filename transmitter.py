import socket
import sys
import select
import cryptSettings
import cryptASCII

# Setting Imports (Look at cryptSettings.py for more info)
cryptText = ""
decryptText = ""
dis = cryptSettings.displacement()
host = cryptSettings.hostClient()
port = cryptSettings.port()
recvBuffer = cryptSettings.recvBuffer()
# Sockets Setup
net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
net.connect((host, int(port)))
sys.stdout.write("--> ")
sys.stdout.flush()

def transmitter():
	while 1:
                # Read, Write, Execute
		r, w, x = select.select([sys.stdin, net], [], [])
		if not r:
			continue
		if r[0] is sys.stdin:
			message = raw_input()
			# Uses my custom python library cryptASCII to encrypt it's messages before their sent
			cryptText = cryptASCII.encrypt(message, dis)
			if message == "quit":
				net.close()
				break
		net.send(cryptText)
		sys.stdout.write("--> ")
		sys.stdout.flush()
	else:
                # Leftover code from when this python file was a client for a chatroom program (Best to leave in just in case the client crashes)
		data = net.recv(recvBuffer)
		decryptText = cryptASCII.decrypt(data, dis)
		print "message from server: ", decryptText
if __name__ == "__main__":

    sys.exit(transmitter())
