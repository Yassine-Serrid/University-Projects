import time
import math
global coinresult
coinresult = []
coins = [5, 10, 20, 50, 100]

def minCountOfCoints(N):
    numbers, Coins = (N + 1) * [0], (N + 1) * [0]
    for i in range(1, N + 1):
        numbers[i] = math.inf
        Coins[i] = -1
    for i in range(0, len(coins)):
        for j in range(1, N + 1):
            if j >= int(coins[i]):
                if numbers[j - (int(coins[i]))] + 1 < numbers[j]:
                    numbers[j] = 1 + numbers[j - int(coins[i])]
                    Coins[j] = i
    printCoinCombination(Coins, coins)
    return numbers[N]


def minCountOfCoints2(N):
    if N == 5:
        minCountOfCoints(N)
    elif N == 10:
        coinresult.append(5)
        N = N - 5
        minCountOfCoints(N)
    elif N > 10:
        coinresult.append(5)
        coinresult.append(5)
        N = N - 10
        numbers, Coins = (N + 1) * [0], (N + 1) * [0]
        for i in range(1, N + 1):
            numbers[i] = math.inf
            Coins[i] = -1
        for i in range(0, len(coins)):
            for j in range(1, N + 1):
                if j >= int(coins[i]):
                    if numbers[j - (int(coins[i]))] + 1 < numbers[j]:
                        numbers[j] = 1 + numbers[j - int(coins[i])]
                        Coins[j] = i
        printCoinCombination(Coins, coins)
        return numbers[N]

def printCoinCombination(Coins, coins):
    coinsRes = {coin:0 for coin in coins}
    start = len(Coins) - 1
    while start != 0:
        j = Coins[start]
        coinsRes[coins[j]] += 1
        start -= int(coins[j])
    for coin in coins:
        if coin != 0 and coinsRes[coin] != 0:
            for i in range(coinsRes[coin]):
                coinresult.append(coin)
    coinresult.sort()
    coinresult.reverse()
    for i in range(len(coinresult)):
        if i < len(coinresult) -1:
            print(coinresult[i], end = " Fils, ")
        else:
            print(coinresult[i], end = " Fils.")




def main():
    N = int(input("Enter the number: "))
    print("The Following is minimal number",
          "of change for", N, "Fils: ", end = "")
    minCountOfCoints2(N)


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    elapsed_time = et - st
    print('\nExecution time:', elapsed_time, 'seconds')