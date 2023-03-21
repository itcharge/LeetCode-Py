class Solution:
    def multiplePack(self, weight: [int], value: [int], count: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(1, W + 1):
                # 枚举第 i 种物品能取个数
                for k in range(min(count[i - 1], w // weight[i - 1]) + 1):
                    # dp[i][w] 取所有 dp[i - 1][w - k * weight[i - 1] + k * value[i - 1] 中最大值
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - k * weight[i - 1]] + k * value[i - 1])
                    
        return dp[size][W]