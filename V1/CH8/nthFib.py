def nthFibonacci_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return nthFibonacci_naive(n-1) + nthFibonacci_naive(n-2)


def nthFibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    memo = [None] * n
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n-1] + memo[n-2]


if __name__ == '__main__':
    # print(nthFibonacci_naive(40))
    print(nthFibonacci_dp(40))
