def zigzag(arr):
    for i in range(0,len(arr) - 1 ):
        if i%2 == 0 and arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

        elif i%2 != 0 and arr[i] < arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]


    return arr

arr = [3,4,7,8,6,2,1]
result = zigzag(arr)
print (result)