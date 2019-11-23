def insertionsort(Alist):
    for i in range (1,len(Alist)):
        k=Alist[i]
        j=i-1
        while j>0 and k<Alist[j]:
            Alist[j+1]=Alist[j]
            j-=1
        Alist[j+1]=k
    
arr = [12, 11, 13, 5, 6] 
insertionsort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 
