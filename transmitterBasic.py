import socket
import sys
import select
import cryptSettings
import cryptASCII

cryptText = ""
decryptText = ""
dis = cryptSettings.displacement()
host = cryptSettings.hostServer()
port = cryptSettings.port()
recvBuffer = cryptSettings.recvBuffer()
net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
net.connect((host, int(port)))
sys.stdout.write("--> ")
sys.stdout.flush()

def transmitter():
	while 1:
		r, w, x = select.select([sys.stdin, net], [], [])
		if not r:
			continue
		if r[0] is sys.stdin:
			message = raw_input()
			#cryptText = cryptASCII.encrypt(message, dis)
			if message == "quit":
				net.close()
				break
		net.send(message)
		sys.stdout.write("--> ")
		sys.stdout.flush()
	else:
		data = net.recv(recvBuffer)
		#decryptText = cryptASCII.decrypt(data, dis)
		print "message from server: ", data
if __name__ == "__main__":

    sys.exit(transmitter())
