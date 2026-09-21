# program to count number of digits entered

num=int(input("Enter any number : "));

count=0;

while num > 0:
    num=num // 10
    count++ 

print("The digit count is : ",count)




