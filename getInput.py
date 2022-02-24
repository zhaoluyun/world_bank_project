f= open('1210320-Asia-Yekaterinburg.csv','r')


for i in range(0,37):
    #print(i)
    n = 0
    out = open('input/input_'+str(i)+'.csv','w')
    while n < 10000:
        line = f.readline()
        if not line:
            break
        out.write(line)
        n+=1
    out.close()




f.close()
