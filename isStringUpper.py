def is_uppercase(inp):
    if inp.isupper() == True:
       return True
    else:
       return False

if __name__ == "__main__":
    inp = input()
    answer = is_uppercase(inp)
    print(answer)
