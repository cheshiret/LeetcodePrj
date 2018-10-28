ilist=[1,2,3,4]
for i in range(len(ilist)):
    for j in range(i+1,len(ilist)):
        if ilist[i] + ilist[j] == 5:
            print [i,j]
        #print ilist[i],ilist[j]