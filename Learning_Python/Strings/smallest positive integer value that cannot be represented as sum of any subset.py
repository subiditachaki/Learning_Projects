def smallest_positive_integer(a):
    n = len(a)
    res = 1
    i=0
    while i < n and a[i] <= res:
        res = res + a[i]
        i+=1

    return res

# a = [1, 3, 6, 10, 11, 15]
a = [1, 1, 1, 1]
print(smallest_positive_integer(a))