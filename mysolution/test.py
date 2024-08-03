from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lens = len(nums)
        i = j = 0
        while(1):
            while(nums[i] != 0 and i < lens-1):   # 找0
                i += 1
            while(nums[j] == 0 and j < lens-1):   # 找非0 
                j += 1
            # 找到第一个非0 与 0 后交换位置判断  且如果i 小于j才能交换不然就会导致 0跑到左边去
            if (i < j):
                nums[i], nums[j] = nums[j], nums[i]
                if j == lens-1: # 如果是最后一个j那么就break
                    break  
            else:
                if(j < lens-1):
                    j += 1
                else:
                    break # j 超了
            # 交换完后原来的零位置处是非零的进入后面的循环会发生继续找下一个零 原来是非零的位置处的是0那么就会去找非零的
            # 所以不用再对i，j加一了 
            # 但是如果没有发生交换那么就会一直呆着不能下一步
        print(nums)

a = Solution()
a.moveZeroes([1])