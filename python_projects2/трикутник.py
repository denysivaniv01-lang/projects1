n = 5
for i in range(1, n + 1):
    numbers = " ".join(str(x) for x in range(1, i + 1))

    spaces = " " * (n - i)
    
    print(spaces + numbers)
