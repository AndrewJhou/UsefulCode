def classic_01_backpack(weights, values, limit_w):
    count_ = len(weights)
    dp = [[0] * (limit_w + 1) for r in range(count_ + 1)]

    for i in range(1, count_ + 1):
        for j in range(1, limit_w + 1):
            # 如果放
            value1 = values[i - 1] + dp[i - 1][j - weights[i - 1]] if j - weights[i - 1] >= 0 else 0
            # 如果不放
            value2 = dp[i - 1][j]
            dp[i][j] = max(value1, value2)

    return dp[count_][limit_w]


if __name__ == '__main__':
    # weights = [4, 3, 1]
    # values = [3000, 2000, 1500]
    # all_w = 4
    # print(classic_01_backpack(weights, values, all_w))

    """
    有空间复杂度的继续优化
    https://www.cnblogs.com/kkbill/p/12081172.html
    https://www.jianshu.com/p/a66d5ce49df5
    """
    # weights = [int(r) for r in input().split()]
    # values = [int(r) for r in input().split()]
    # # 总重量
    # all_w = int(input())

    weights = [4, 3, 1]
    values = [3000, 2000, 1500]
    all_w = 4

    # 物品个数
    count_ = len(weights)
    dp = [[0] * (all_w+1) for r in range(count_+1)]
    for i in range(1, count_+1):
        for j in range(1, all_w+1):
            # 如果放
            value1 = values[i-1] + dp[i-1][j-weights[i-1]] if weights[i-1] - j <= 0 else 0
            # 不放
            value2 = dp[i-1][j]
            dp[i][j] = max(value1, value2)

    print(dp[count_][all_w])
