import osmapi as osm
api = osm.OsmApi()
import time

def inbox(lng,lat,city):
    if lng < city[1][0] and lng > city[0][0] and lat < city[0][1] and lat > city[1][1]:
        return True
    else:
        return False


def track(inputfilename,outputfilename_lipetsk,outputfilename_perm,out_error_name):

    f = open(inputfilename+'.csv','r')
    out_lipetsk = open(outputfilename_lipetsk+'.csv','w')
    out_perm = open(outputfilename_perm+'.csv','w')
    out_error = open(out_error_name+'.csv','w')

    #Lipetsk and Perm
    lipetsk = [[37.507324,53.683695],[40.957031,51.767839]] #lefthead,rightbottom
    #39.3434,52.7521;39.9442,52.4794 城市
    #[37.507324,53.683695],[40.957031,51.767839] 州
    perm = [[51.525878,61.825040],[59.677734,56.035225]] 
    #55.6293,58.2611;56.8309,57.7855 城市
    #[51.525878,61.825040],[59.677734,56.035225] 州
    

    #把两个城市里的道路分别筛出来，合并到两个文件

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

        if inbox(lng1,lat1,lipetsk) or inbox(lng2,lat2,lipetsk):
            out_line = '%f,%f,%f,%f,' % (lng1,lat1,lng2,lat2)
            out_lipetsk.write(out_line)
            out_lipetsk.write(l)

        if inbox(lng1,lat1,perm) or inbox(lng2,lat2,perm):
            out_line = '%f,%f,%f,%f,' % (lng1,lat1,lng2,lat2)
            out_perm.write(out_line)
            out_perm.write(l)

    f.close()

    out_lipetsk.close()
    out_perm.close()
    out_error.close


    #平均速度7*24分布
    #周一-周五早、晚高峰时间算出来
    #周末高峰时间算出来