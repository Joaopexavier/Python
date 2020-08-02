def positive_sum(arr):
    u = 0  
    for num in arr:
        if num > 0:
           u += num
        else: 
             u += 0  
    return u

if __name__ == "__main__":
  times = int(input("How much numbers has in this list? "))
  arr = []
  for i in range(0, times):
    number = int(input("Number {}: ".format((i + 1))))
    arr.append(number)
  answer = positive_sum(arr)
  print(answer)
