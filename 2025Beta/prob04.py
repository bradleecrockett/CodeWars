# iterates through all values from 2 to n/2 and checks if n is divisible by any of them
# result determines if the num is prime or not
def is_Prime(n: int) -> bool:
    if n <= 1: return False

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

num: int = int(input())

# Check if the number is prime
if is_Prime(num):
    print(f"{num} is already prime")
else:
    # check if the number ahead or behind is prime
    if (is_Prime(num + 1) or is_Prime(num - 1)):
        print(f"{num} could be a prime!")
    else:
        print(f"{num} is a bad test specimen")