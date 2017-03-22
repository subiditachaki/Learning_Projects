a = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]

def sort_array(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
    return(a)

def sub_array(a,start):
    count = 1
    i = 0
    for i in range(start,len(a)):
        if (i + 1) < len(a) and a[i+1] == a[i] + 1 :
            count += 1
        else :
            break
    return(i, count)

def largest_contagious(a):
     a = sort_array(a)

     # print ("sorted array - " + str(a))
     largest_count = 1
     j = -1
     i = 0
     while j+1 < len(a):
         i = j + 1
         # print("count starting at position - " + str(i))
         j,count = sub_array(a,i)
         # print("count ending at position - " + str(j))

         if count > largest_count:
             largest_count = count
         # print("largest contagious subarray length - " + str(largest_count))
     print("final largest count - " + str(largest_count))

largest_contagious(a)