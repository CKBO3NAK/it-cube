a = int(input())
if a < 1 or a>10:
    print("ошибка")
else:
    if a == 1 or a == 2 or a == 3:
        print("I"*a)
    elif a == 5 or a == 6 or a == 7 or a == 8:
        print("V"+"I"*(a-5))
    elif a == 9 or a == 10:
        print("I"*(10-a)+"X")
    
    
