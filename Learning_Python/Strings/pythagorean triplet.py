import math

def square_elements(a):
    for i in range(0,len(a)):
        a[i] = a[i]*a[i]
    return a

def sort_array(a):
    for i in range(0,len(a)):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                a[j],a[i] = a[i],a[j]
    return a

def pythagorean_triplet(a):

    a = sort_array(square_elements(a))
    # print (' a = ' + str(a))
    flag = 0
    for i in range(0,len(a)):
        # print ('iteration = ' + str(i))
        l,r = (i + 1) , (len(a) - 1)
        # print (' l = ' + str(l) + ' r = ' + str(r))
        while l < r:
            # print (' a[i] = ' + str(a[i]) + ' , a[r] = ' + str(a[r]) + ' , a[l] = ' + str(a[l]))
            if a[i] == a[l] + a[r]:
                print("("+str(int(math.sqrt(a[i])))+" , "+str(int(math.sqrt(a[l])))+" , "+str(int(math.sqrt(a[r])))+")")
                if flag == 0:
                    flag = 1
                break
            elif a[i] > a[l] + a[r]:
                r-=1
            else :
                l+=1
    if flag == 0:
        print('False')


a = [3, 4,6,1, 5]
pythagorean_triplet(a)
a = [10, 4, 6, 12, 5]
pythagorean_triplet(a)