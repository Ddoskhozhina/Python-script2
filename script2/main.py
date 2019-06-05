# Even/odd number checker
num = int(input("Enter a number(odd/even): "))

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

# Prime number checker
num = int(input("Enter a number(prime number): "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
