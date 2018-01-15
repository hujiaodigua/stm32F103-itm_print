import time
import socket
import gdb
from cmdebug import dwt_gdb


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


gdb.execute('monitor resume')
time.sleep(2)

D = dwt_gdb.DWT()
dr = D.read(0x2000044c)
print(dr)

dr = D.invoke(help)
