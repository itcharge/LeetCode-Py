def boyerMoore(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    bc_table = generateBadCharTable(p)              # 生成坏字符位置表
    gs_list = generageGoodSuffixList(p)             # 生成好后缀规则后移位数表
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j > -1 and T[i + j] == p[j]:
            j -= 1
        if j < 0:
            return i
        bad_move = j - bc_table.get(T[i + j], -1)
        good_move = gs_list[j]
        i += max(bad_move, good_move)
    return -1
            
    
# 生成坏字符位置表
def generateBadCharTable(p: str):
    bc_table = dict()
    
    for i in range(len(p)):
        bc_table[p[i]] = i                          # 坏字符在模式串中最后一次出现的位置
    return bc_table

# 生成好后缀规则后移位数表
def generageGoodSuffixList(p: str):
    # 好后缀规则后移位数表
    # 情况 1: 模式串中有子串匹配上好后缀
    # 情况 2: 模式串中无子串匹配上好后缀，但有最长前缀匹配好后缀的后缀
    # 情况 3: 1，2 都不成立
    
    m = len(p)
    gs_list = [m for _ in range(m)]
    suffix = generageSuffixArray(p)
    j = 0
    for i in range(m - 1, -1, -1):
        if suffix[i] == i + 1:
            while j < m - 1 - i:
                if gs_list[j] == m:
                    gs_list[j] = m - 1 - i
                j += 1
        
    for i in range(m - 1):
        gs_list[m - 1 - suffix[i]] = m - 1 - i
    
    return gs_list

def generageSuffixArray(p: str):
    m = len(p)
    suffix = [m for _ in range(m)]
    for i in range(m - 2, -1, -1):
        start = i
        while start >= 0 and p[start] == p[m - 1 - i + start]:
            start -= 1
        suffix[i] = i - start
    return suffix

print(boyerMoore("abbcfdddbddcaddebc", "bcd"))
print(boyerMoore("", ""))