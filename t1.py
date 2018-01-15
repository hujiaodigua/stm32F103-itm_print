import gdb
import time
import socket


c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('192.168.0.101',8080))
   
time.sleep(1)
gdb.execute('target remote localhost:3333')
gdb.execute('monitor reset')
gdb.execute('monitor halt')
gdb.execute('load')
time.sleep(1)


while(1):
    control_data = c.recv(64)
    response = gdb.execute(control_data,to_string=True)
    print(response)
    c.send(response)
    
    #time.sleep(1)


'''
s_response = gdb.execute('s',to_string=True)
print(s_response)
c.send(s_response)

s_response = gdb.execute('s',to_string=True)
print(s_response)
c.send(s_response)

l_response = gdb.execute('s',to_string=True)
print(l_response)
c.send(l_response)
#print(type(s_response))
'''
