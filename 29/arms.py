num=int(input("enter num"))

def palindrome(num):
    return str(num)==str(num)[::-1]

def armstrong(num):
    temp = str(num)
    power = len(temp)
    arms = sum(int(a) ** power for a in temp)
    return arms == num

def automorphic(num):
    square=num**2
    return str(square).endswith(str(num))
        


if palindrome(num):
    print("its palindrome")
else:
    print("not palindrome")

if armstrong(num):
    print("its armstrong")
else:
    print("not armstrong")

if automorphic(num):
    print("its automorphic")
else:
    print("not automorphic")
