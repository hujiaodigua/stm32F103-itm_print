import gdb
import time
import socket
import telnetlib
import asyncio

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.100',8080))

time.sleep(1)
gdb.execute('target remote localhost:3333')
gdb.execute('monitor reset')
gdb.execute('monitor halt')
gdb.execute('load')
time.sleep(1)

@asyncio.coroutine
def debug():
    if(s.recv(64) == b'debug_end'):
        s.send(b'debug_end ok!!!')
        break
    else if(s.recv(64) == b'debug_start'):
        s.send(b'debug_start ok!!!')
        control_data = s.recv(64)
        response = gdb.execute(control_data,to_string=True)
        print(response)
        s.send(response)
        
@asyncio.coroutine
def mem():
    if(s.recv(64) == b'mem_end'):
        s.send(b'mem_end ok!!!')
        break
    else if(s.recv(64) == b'mem_poll'):
        s.send(b'mem_poll ok!!!')
        response_mem = gdb.execute('monitor mdw 0x2000044c',to_string=True)
        print(response_mem)
        s.send(response_mem)
        time.sleep(3)

loop = asyncio.get_event()
tasks = [debug(),mem()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
