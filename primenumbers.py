n = int(input("Enter a number:"))
prime = n

if n % 1 == 0 and n % n == 0:
    print(f"{prime} is a prime number")
else:
    print(f"{prime} is not a prime number")