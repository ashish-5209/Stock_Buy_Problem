
def stockBuySell(A,n):
    ##Your code here
    if n == 0 or n == 1:
        print("No Profit", end = " ")
        return
    
    local_min = []
    local_max = []
    if A[0] < A[1]:
        local_min.append(0)
    for i in range(1,n-1):
        if A[i] < A[i-1] and A[i] < A[i+1]:
            local_min.append(i)
        if A[i] > A[i-1] and A[i] > A[i+1]:
            local_max.append(i)
    if A[n-1] > A[n-2]:
        local_max.append(n-1)
    i = 0
    j = 0
    profit = 0
    while i < len(local_min) and j < len(local_max):
        print("("+ str(local_min[i]) + " " + str(local_max[j]) +")", end=" ")
        profit += A[local_max[j]] - A[local_min[i]]
        i+=1
        j+=1
    if profit <= 0:
        print("No Profit", end="")
