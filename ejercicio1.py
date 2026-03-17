def main(n):
    for i in n:
        printPattern(i)
        print()

def printPattern(n):
    for i in range(n):
        for j in range(n):
            if (i == 0) or (i == (n - 1)) or (j == n-1):
                print("*", end="")
                continue
            if i == 1 or (j != 0 and i == n - 2):
                print(".", end="")
                continue
            if j == n - 2:
                print(".", end="")
            if j == 0:
                print("*", end="")
                continue

            if i < n // 2 + 1:
                if (i % 2 == 0 and j < n - i) or (i == j):
                    print("*", end="")
                if i % 2 != 0 and j < n - i:
                    print(".", end="")
            # if i > n // 2:


            # else:
            #     print(".", end="")
        # elif (i % 2 != 0):
        #     print("." * n, end="")
        print()

if __name__ == "__main__":
    t = int(input())
    n = [int(input()) for _ in range(t)]
    main(n)
