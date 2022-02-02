# KMP 匹配算法，T 为文本串，p 为模式串
def kmp(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    next = generateNext(p)                  # 生成 next 数组
    
    i, j = 0, 0
    while i < n and j < m:
        if j == -1 or T[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == m:
        return i - j
    
    return -1
            
    
# 生成 next 数组
# next[i] 表示坏字符在模式串中最后一次出现的位置
def generateNext(p: str):
    m = len(p)
    
    next = [-1 for _ in range(m)]           # 初始化数组元素全部为 -1
    i, k = 0, -1
    while i < m - 1:                        # 生成下一个 next 元素
        if k == -1 or p[i] == p[k]:
            i += 1
            k += 1
            if p[i] == p[k]:
                next[i] = next[k]           # 设置 next 元素
            else:
                next[i] = k                 # 退到更短相同前缀
        else:
            k = next[k]
    return next

print(kmp("abbcfdddbddcaddebc", "aaaaa"))
print(kmp("abbcfdddbddcaddebc", "bcf"))
print(kmp("aaaaa", "bba"))
print(kmp("mississippi", "issi"))
print(kmp("ababbbbaaabbbaaa", "bbbb"))