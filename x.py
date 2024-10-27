



sum_=0
while True:
    num=input("enter a num or 'x' to stop")
    if num.lower()=='x':
        break
    
    try:
        num_enter=int(num)
        sum_+=num_enter
    except error:
        print("enter a valid num")
    
   
print("the sum of all nums is",sum_)
