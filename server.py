import socket

sock = socket.socket()
sock.bind(('', 9090))
print("Server started working")
sock.listen(0)
print("Server started listening")
conn, addr = sock.accept()
print("Connected client ", addr)

msg = ''

while True:
	print("Taking data from client")
	data = conn.recv(1024)
	if not data:
		print("Client didn't send data")
		break
	msg += data.decode()
	print("Sending data to client")
	conn.send(data)

print(msg)

conn.close()
print("Disconnection client")
sock.close()
print("Shutdown server")