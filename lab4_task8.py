def allfiles(dirf):
    import os 
    masterlist=[]
    for x,y,z in os.walk(dirf):
        if len(z)>0:
            for i in z:
                if i[-1]=='3':
                    masterlist.append(x+'/'+i)
    return masterlist
	
def find_dups(masterlist):
    import os
    d=dict()
    for x in masterlist:
        import string
        x=x.replace(' ','\ ')
        for i in "(){}[]&,';":
            x=x.replace(i,"\\"+i)
        f=os.popen('md5sum '+x)
        hashed=f.read()
        d[hashed[:32]]=d.get(hashed[:32],[])+[x]
        f.close()
        print x
    return d
