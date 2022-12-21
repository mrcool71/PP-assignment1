def palindrome(num):
    number=int(num)
    num=number
    reversed_number =0
    while (num!=0):
        r=num%10
        num=num//10
        reversed_number=reversed_number*10+r
    if (reversed_number==number):
        print ("True")
    else :
        print ("False")

given_string=str(input("Enter the string"))
palindrome(given_string)


