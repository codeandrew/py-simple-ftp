import socket
import os 
import threading

def retrieve_file(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS : {}".format(str(os.path.getsize(filename))))
        user_response = sock.recv(1024)
        if user_response[:2] == 'ok':
            with open(filename, 'rb') as f:
                bytes_to_send = f.read(1024)
                sock.send(bytes_to_send)
                while bytes_to_send != "":
                    bytes_to_send = f.read(1024)
                    sock.send(bytes_to_send)

    else:
        sock.send("Error")
    sock.close()

def main():
    host = '127.0.0.1'
    port = 4444

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)
    print("Server Started. ")
    while True:
        c, addr = s.accept()
        print("client connected ip: {}".format(str(addr)))
        t = threading.Thread(target=retrieve_file, args=("retrieve_thread", c))
        t.start()

    s.close()

if __name__ == '__main__':
    main()
