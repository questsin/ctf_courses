# coding=utf-8
import socket

PORT = 9999
SERVER = '54.148.158.108'
MESSAGE  = "hello kokc!"

#возвращаем объект сокета
s = socket.socket()
#коннектимся к серверу
s.connect((SERVER,PORT))
#отправляем сообщение
s.send(MESSAGE)
#читаем ответ от сервера
data = s.recv(1024)
print data
#закрываем соедениение
s.close()


