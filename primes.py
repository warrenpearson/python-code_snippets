import sys

def isPrime(n):
    if n <= 1:
        return False
    if n < 3:
        return True
    if (n % 2 == 0):
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if (n % i == 0):
            return False
    return True

end_num = int(sys.argv[1])

for i in range(0, end_num):
    if isPrime(i):
        print(i, end=" ")

print("")
