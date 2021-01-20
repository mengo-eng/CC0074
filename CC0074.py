divs = []
n = int(input("Enter a number: "))
for i in range(2, n+1):
    if n % i == 0:
        divs.append(i)
if len(divs) < 2 and n != 1:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

