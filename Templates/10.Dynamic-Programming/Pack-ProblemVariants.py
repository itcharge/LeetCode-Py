class Solution:
    # 完全问题求方案总数
    def zeroOnePackNumbers(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                dp[w] = sum(dp[w], dp[w - weight[i - 1]])
                
        return dp[W]
    
    # 完全问题求最优方案数
    def zeroOnePackNumbers(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        op = [[1 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                    op[i][w] = op[i - 1][w]
                else:
                    if dp[i][w] < dp[i][w - weight[i - 1]] + value[i - 1]:
                        dp[i][w] = dp[i][w - weight[i - 1]] + value[i - 1]
                        op[i][w] = op[i][w - weight[i - 1]]
                    elif dp[i][w] == dp[i][w - weight[i - 1]] + value[i - 1]:
                        op[i][w] = op[i - 1][w] + op[i][w - weight[i - 1]]
                    
        return (dp[size][W], op[size][W])