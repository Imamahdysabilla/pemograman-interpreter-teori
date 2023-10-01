def hollow_hourglass_pattern(n):
#Batas
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(n - i):
            print(" ", end=" ")
        print()
#bawah
    for i in range(2, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(n - i):
            print(" ", end=" ")
        print()

n = 5
hollow_hourglass_pattern(n)
