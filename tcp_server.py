import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    # Creating a socket and binding it to our host and port.
    s = socket.socket()
    s.bind((host, port))

    s.listen(1) # listening to one connection at a time.

    c, addr = s.accept()
    print("Connection from: "+ str(addr))
    while True:
        # transferring 1024 bytes at a time.
        # since the data will come in raw bytes, use decode('utf-8')
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user: " +data)
        data = data.upper()

        print("Sending: "+data)

        c.send(data.encode('utf-8'))

    c.close()

if __name__ == '__main__':
    Main()
