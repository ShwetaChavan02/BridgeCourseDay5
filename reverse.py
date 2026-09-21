# Program to reverse the given number

num = int(input("Enter any number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")