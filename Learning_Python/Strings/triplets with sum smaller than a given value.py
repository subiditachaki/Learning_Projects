def sort(arr):

    length = len(arr)
    print (length)
    for i in range(0 , length):
        j = i+1

        while j < length:
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            j += 1


    return arr

def checktriplet(unsorted_arr):
    arr = sort(unsorted_arr)
    x = 5
    for i in range(0,len(arr)):
        j=i+1
        if arr[i] > x or (arr[i]+arr[j] > x):
            break

        while j <(len(arr) - 1):
            k = j+1
            if arr[j] > x or (arr[j]+arr[k] > x):
                break

            while k < (len(arr)-2):
                if arr[i]+arr[j]+arr[k] == x:
                    print ("("+str(arr[i])+","+str(arr[j])+","+str(arr[k])+")")
                elif  arr[k] > x or (arr[i]+arr[j]+arr[k] > x):
                    break

                k+=1
            j+= 1
# Driver program to test the above function
checktriplet([5,1,2,6,3,4,0,-1,7])
