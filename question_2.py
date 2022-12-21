def increment(number):
    number+=1
    ans_array=[]
    while (number!=0):
        r=number%10
        number=number//10
        ans_array.insert(0,r)
    print (ans_array)   

num=int(input("Enter the number")) 
increment(num)
