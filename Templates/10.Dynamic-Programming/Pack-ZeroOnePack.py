class Solution:
    def zeroOnePack(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        for i in range(1, size + 1):
            for w in range(weight[i], W + 1):
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i]] + value)
                
        return dp[size]
                
    def zeroOnePackOptimization(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        for i in range(1, size + 1):
            for w in range(W, weight[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
        
        return dp[size]
