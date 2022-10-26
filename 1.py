num = 10
if num > 1:

    for i in range(3, int(num / 2) + 1):
        if (num % i + 1) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")

elif num == 1:
    print(num, "is neither composite nor prime number.")
else:
    print(num, "is not a prime number")
