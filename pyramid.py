# print a pyramid star pattern
# parameter passing range(1,5) starts with 1 and ends at 4...o/p(1,2,3,4)
# range(1,6,2)starts with 1, ends at 5 and adds 2 at each number...o/p(1,2,5)
# range(5,1,-1) starts with 5, ends at 1 substracts 1 at each step...o/p(5,3,2)

for i in range(1,5):
    for j in range(1,(4-i)+1):
        #starts from 1 then row(i)-1 and then increment the column number
        print(" ",end="") 
        #end="" does not take new line after ending print statement

# logic relation between row and starts 
# row no. x 2 - 1 = no. of starts
    for k in range(1,(i * 2 - 1)+1):
        print("*",end="")
    print()