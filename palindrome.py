n = int(input("Enter a number:"))
original = n
reversed = 0
while n > 0:
    digit = n % 10
    reversed = reversed * 10 + digit
    n = n // 10
if reversed == original:
    print(f"The given number {original} is  a palindrome")
else:
    print(f"{original} is not a palindrome")
