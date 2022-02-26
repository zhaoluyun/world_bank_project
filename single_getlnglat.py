import osmapi as osm
api = osm.OsmApi()
import time

def inbox(lng,lat,city):
    if lng < city[1][0] and lng > city[0][0] and lat < city[0][1] and lat > city[1][1]:
        return True
    else:
        return False


def track(inputfilename,outputfilename,out_other_name,out_error_name):

    f = open(inputfilename+'.csv','r')
    out = open(outputfilename+'.csv','w')
    out_other = open(out_other_name+'.csv','w')
    out_error = open(out_error_name+'.csv','w')

    #box
    #volgograd = [[43.9872,48.9358],[44.8500,48.3705]] #lefthead,rightbottom
    omsk = [[72.8586,55.5084],[73.8638,54.7516]] #lefthead,rightbottom


    for l in f.readlines():
        
        a = l.split(',')
        n1 = a[0]
        n2 = a[1]

        try:
            node1 = api.NodeGet(n1)
        except:
            out_error.write(l)
            continue
        time.sleep(0.1)

        lng1 = node1['lon']
        lat1 = node1['lat']

        try:
            node2 = api.NodeGet(n2)
        except:
            out_error.write(l)
            continue
        time.sleep(0.1)

        lng2 = node2['lon']
        lat2 = node2['lat']

        if inbox(lng1,lat1,omsk) or inbox(lng2,lat2,omsk):
            out_line = '%f,%f,%f,%f,' % (lng1,lat1,lng2,lat2)
            out.write(out_line)
            out.write(l)

        else:
            out_line = '%f,%f,%f,%f,' % (lng1,lat1,lng2,lat2)
            out_other.write(out_line)
            out_other.write(l)

    f.close()

    out.close()
    out_other.close()
    out_error.close()

