def rabinKarp(T: str, p: str) -> int:
    len1, len2 = len(T), len(p)
    
    hash_p = hash(p)
    for i in range(len1 - len2 + 1):
        hash_T = hash(T[i: i + len2])
        if hash_p != hash_T:
            continue
        k = 0
        for j in range(len2):
            if T[i + j] != p[j]:
                break
            k += 1
        if k == len2:
            return i
    return -1

print(rabinKarp("abcdeabc", "bcd"))