def two_sum(list_1,target):
    for i in range (len(list_1)):
        remainder=target -list_1[i]
        if remainder in list_1:
            index_1=list_1.index(remainder)
            ans_list=[i,index_1]
            print (ans_list)
            break
listsss=[]
n=int(input("Enter value for n:"))
for j in range(n):
    element=int(input("Enter element:"))
    listsss.append(element)

val=int(input("Enter the sum"))
 

two_sum(listsss,target=val)  
