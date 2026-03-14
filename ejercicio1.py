def main(n):
    for i in n:
        printPattern(i)

def printPattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == (n - 1):
                print("x", end="")
            elif j == n-1:
                print("*", end="")
            elif i == 1:
                print(".", end="")
        # elif (i % 2 != 0):
        #     print("." * n, end="")
        print()

if __name__ == "__main__":
    t = int(input())
    n = [int(input()) for _ in range(t)]
    main(n)
