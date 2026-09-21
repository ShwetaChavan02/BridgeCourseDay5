
# Program to reverse the given number

num = int(input("Enter any number: "))
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse of the given number is:", reverse)

