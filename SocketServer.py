# coding=utf-8
import socket

#порт
PORT = 9999
#получаем объект сокета
s = socket.socket()
#привязываем слушать сокет определенный порт
s.bind(('', PORT))
#устанавливаем максимальное количество клиентов в очереди. При привышении количества. Клиентам будет отказано в подключении
s.listen(5)
while True:
    conn, addr = s.accept()
    print(addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        conn.send("reply, from " + data)

