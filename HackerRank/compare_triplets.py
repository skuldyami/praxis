def compareTriplets(a, b):
    a_count=0
    b_count=0
    for i in range(len(a)):
        if a[i]>b[i]:
            a_count+=1
        elif b[i]>a[i]:
            b_count+=1
    return [a_count, b_count]