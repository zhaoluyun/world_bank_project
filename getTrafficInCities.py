import socket

timeout = 20
socket.setdefaulttimeout(timeout)

import threading
import single_getlnglat

thread_list = [] 


for i in range(0,37):
    inputfilename = 'input/input_'+str(i)
    outputfilename_lipetsk = 'output/output_lipetsk_'+str(i)
    outputfilename_perm = 'output/output_perm_'+str(i)
    out_error_name = 'output/error_'+str(i)

    t=threading.Thread(target=single_getlnglat.track,args=(inputfilename,outputfilename_lipetsk,outputfilename_perm,out_error_name,)) # 创建子线程
    thread_list.append(t)


for t in thread_list:
    t.start() 

for t in thread_list:
    t.join()  


