f= open('1210320-Asia-Yekaterinburg.csv','r')
'''
n=0
while n<5028:
    f.readline()
    n+=1
'''

for i in range(24,37):
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
