a = list(map(int,input().split()))
min=a[0]
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        min_ind = i
        
a[0],a[min_ind] = a[min_ind], a[0]
print(*a)