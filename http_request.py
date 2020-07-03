import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  # website : data.pr4e.org, port : 80

# encode converts from unicode internally to UTF-8
# b'' and .encode() are equivalent.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # receive every 512-characters of data, i.e. the recv() returns an empty string
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
