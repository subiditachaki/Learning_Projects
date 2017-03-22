# For Example
# A = {10, 15, 25}
# B = {1, 5, 20, 30}
#
# The resulting arrays are:
# 10 20
# 10 20 25 30
# 10 30
# 15 20
# 15 20 25 30
# 15 30
# 25 30

def sorted_2_element_array(num, arr2):
    new_arr = [num]
    for j in arr2:
        if j > num:
            new_arr.append(j)
            print(new_arr)
            new_arr = [num]


def multi_element_array(i, num,arr1,arr2):

    arr1_count = i + 1
    arr2_count = 0

    create_element = 1

    new_arr = [num]

    while arr1_count <= len(arr1) and arr2_count <= len(arr2):

        if create_element%2 != 0:
            for count in range(arr2_count, len(arr2)):
                if arr2[count] > new_arr[create_element - 1]:
                    new_arr.append(arr2[count])
                    create_element += 1
                    break
            arr2_count = count + 1

            # print ("arr2_count - " + str(arr2_count))
        # print ("count - " + str(count))

        if create_element%2 == 0:
            for count in range(arr1_count, len(arr1)):
                # print ("count - " + str(count))
                if arr1[count] > new_arr[create_element - 1]:
                    new_arr.append(arr1[count])
                    create_element += 1
                    break
            arr1_count = count + 1

        # if (arr1_count == len(arr1) and create_element%2 == 0) or (arr2_count == len(arr2) and create_element%2 != 0):
        #     break
            # print ("arr1_count - " + str(arr1_count))

    if len(new_arr) > 2:
        print (new_arr)


def new_sorted_arrays(arr1, arr2):
    for i in range(0,len(arr1)):
        sorted_2_element_array(arr1[i], arr2)
        multi_element_array(i,arr1[i],arr1,arr2)

A = [10, 15, 25]
B = [1, 5, 20, 30]
new_sorted_arrays(A,B)