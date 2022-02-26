f= open('mapbox_data/1213010-Asia-Omsk.csv','r')

i = 0
while i>=0:
    print(i)
    n = 0
    out = open('input_omsk/input_omsk_'+str(i)+'.csv','w')
    while n < 10000:
        line = f.readline()
        if not line:
            i = -2
            break
        out.write(line)
        n+=1
    out.close()
    i += 1
    




f.close()
