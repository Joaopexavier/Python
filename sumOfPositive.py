def positive_sum(arr):
    u = 0  
    for num in arr:
        if num > 0:
           u += num
        else: 
             u += 0  
    return u
