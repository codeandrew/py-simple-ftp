import socket

def main():
    host = '127.0.0.1'
    port = 4444
    s = socket.socket()
    s.connect((host,port))

    filename = raw_input("Filename?:   ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File Exists, {} \
                Bytes, download? (Y/N) ?".format(str(filesize)))
            if message == 'Y':
                s.send('OK')
                f = open('new_{}'.format(filename), 'wb')
                data = s.recv(1024)
                total_receive = len(data)
                f.write(data)
                while total_receive < filesize:
                    data = s.recv(1024)
                    total_receive += len(data)
                    f.write(data)
                    print("{0:.2f}".format( (total_receive/float(filesize))*100 + \
                            "% Done"))
                print("Download Complete! ")
        else:
            print("File does not exist!")


if __name__ == '__main__':
    main()