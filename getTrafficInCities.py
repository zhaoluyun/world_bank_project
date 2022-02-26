import socket

timeout = 20
socket.setdefaulttimeout(timeout)

import threading
import single_getlnglat

thread_list = [] 


for i in range(0,13):
    inputfilename = 'input_omsk/input_omsk_'+str(i)
    outputfilename = 'output_omsk/output_omsk_'+str(i)
    out_other_name = 'output_omsk/omsk_other_'+str(i)
    out_error_name = 'output_omsk/error_'+str(i)

    t=threading.Thread(target=single_getlnglat.track,args=(inputfilename,outputfilename,out_other_name,out_error_name,)) 
    thread_list.append(t)


for t in thread_list:
    t.start() 

for t in thread_list:
    t.join()  


