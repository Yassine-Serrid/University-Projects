import time


def findMin(V):
    deno = [5, 10, 20, 50,
            100]

    n = len(deno)
    ans = []

    if V == 5:
        ans.append(deno[0])

    elif V == 10:
        ans.append(deno[0])
        ans.append(deno[0])

    # Traverse through all denomination
    elif V > 10:
        for i in range(2):
            V = V - 5
            ans.append(5)

        i = n - 1
        while (i >= 0):
            # Find denominations
            while (V >= deno[i]):
                V -= deno[i]
                ans.append(deno[i])

            i -= 1

    ans.sort()
    ans.reverse()
    # Print result
    for i in range(len(ans)):
        if i < len(ans) - 1:
            print(ans[i], end=" Fils, ")
        else:
            print(ans[i], end=" Fils.")


def main():
    n = int(input("Enter the number: "))

    print("The Following is minimal number",
          "of change for", n, "Fils : ", end="")
    findMin(n)


# Driver Code
if __name__ == '__main__':
    st = time.time()
    main()
    et = time.time()
    elapsed_time = et - st
    print('\nExecution time:', elapsed_time, 'seconds')

