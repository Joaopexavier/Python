def greet(name): 
    y = name[0]
    z = name[1::]
    h = z.lower()
    u = y.upper()
    return("Hello {}!".format(u+h))

if __name__ == "__main__":
  name = input()
  answer = greet(name)
  print(answer)
