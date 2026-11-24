# WAP to calculate P(n, r)
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

if n < 0 or r < 0 or r > n:
    print("Invalid input: Ensure that n >= r >= 0.")
else:
    # Using // (integer division) avoids floating-point inaccuracy for large numbers
    res = fact(n) // fact(n - r)
    print(f"The value of P({n}, {r}) = {res}")
