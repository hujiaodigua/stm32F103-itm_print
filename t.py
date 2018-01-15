import gdb
import time
import socket
from cmdebug import dwt_gdbport dwt_gdb


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.100',8080))
#s.setblocking(0)

#The value of the global varaible which in the project
#c_address = 0x2000044c
#a_address = 0x20000014
#b_address = 0x20000018
   
time.sleep(1)
gdb.execute('target remote localhost:3333')
gdb.execute('monitor reset')
gdb.execute('monitor halt')
gdb.execute('load')
time.sleep(1)

while(1):
    s1 = s.recv(64)
    if(s1 == b'debug_start'):
        s.send(b'debug_start ok!!!')
        while(1):
            s2 = s.recv(64)
            if(s2 == b'debug_end'):
                s.send(b'debug_end ok!!!')
                break
            else:
                if(s2 == b'monitor resume'):
                    s.send(b'resume_ok!!!')
                control_data = s2
                response = gdb.execute(control_data,to_string=True)
                print(response)
                s.send(response)
                #time.sleep(1)

    if(s1 == b'mem_poll'):
        s.send(b'mem_poll ok!!!')
        while(1):
            s2 = s.recv(64)
            if(s2 == b'mem_end'):
                s.send(b'mem_end ok!!!')
                break
            if(s2 == b'c_address'):
                response_mem = gdb.execute('monitor mdw 0x2000044c',to_string=True)
                print(response_mem)
                s.send(response_mem)
                time.sleep(2)
            if(s2 == b'a_address'):
                response_mem = gdb.execute('monitor mdw 0x20000014',to_string=True)
                print(response_mem)
                s.send(response_mem)
                time.sleep(2)
            if(s2 == b'b_address'):
                response_mem = gdb.execute('monitor mdw 0x20000018',to_string=True)
                print(response_mem)
                s.send(response_mem)
                time.sleep(2)

                
    if(s1 == b'dwt'):
        s.send(b'dwt ok!!!')
        while(1):
            s2 = s.recv(64)
            if(s2 == b'dwt_end'):
                s.send(b'dwt_end ok!!!')
                break
            else:
                D = dwt_gdb.DWT()
                dr = D.read(0x2000044c)
                control_data = s2
                response = gdb.execute(control_data,to_string=True)
                print(response)
                s.send(response)
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
