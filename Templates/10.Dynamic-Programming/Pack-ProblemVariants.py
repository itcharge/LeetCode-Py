class Solution:
    # 完全问题求解方案总数
    def zeroOnePackNumbers(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                dp[w] = sum(dp[w], dp[w - weight[i - 1]])
                
        return dp[W]