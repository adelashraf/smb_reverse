import socket
import sys
P  = '\033[35m' # purple
W  = '\033[0m'  # white (normal)
O  = '\033[32m' # orange
R  = '\033[31m'
G  = '\033[32m'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
host = raw_input(O+"write your ip  : "+W) 
port = int(raw_input(O+"write the port for listning : "+W))             
s.bind((host, port)) 
a = '\x00\x00\x00U\xffSMBr\x00\x00\x00\x00\x98\x01(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00g\xee\x00\x00\x16\x1d\x11\x03\x00\x03\n\x00\x01\x00\x04\x11\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xfd\xe3\x00\x80\xd2\xb7,\xeb\x83w\xcf\x01\x88\xff\x00\x10\x00\xee\xcb\x81\x8c\x9e<cJ\xaf\x0e\x0c\xed?\xf6\x972'
s.listen(5) 
try :
   while True:
      c, addr = s.accept()     
      print (P +'Got connection from') , addr , W
      data = c.recv(10000)
      print 'data is : ' , repr(data)
      c.send(a)
      c.close()
 
except KeyboardInterrupt :
    print R + "You pressed Ctrl+C" +W
    sys.exit()
except socket.gaierror:
    print R + 'Host did not open plz try to check if that your local ip ' +W
    sys.exit()
except socket.error:
    print R + "Couldn't listning the port maby is used" + W
    sys.exit()
