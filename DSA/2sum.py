arr = [1,2,3,5,8,9,4]
target = 9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==target):
            print(i,j)