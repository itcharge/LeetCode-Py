## 1. 算法思想

> 计数排序（Counting Sort）基本思想：
>
> 使用一个额外的数组 `counts`，其中第 `i` 个元素 `counts[i]` 是待排序数组 `arr` 中值等于 `i` 的元素个数。然后根据数组 `counts` 来将 `arr` 中的元素排到正确的位置。

## 2. 算法步骤

- 找出待排序数组中最大值元素和最小值元素。
- 统计数组中每个值为 `i` 的元素出现的次数，存入数组的第 `i` 项。
- 对所有的计数累加（从 `counts` 中的第一个元素开始，每一项和前一项累加）。
- 反向填充目标数组：将每个元素 `i` 放在新数组的第 `counts[i]` 项，每放一个元素就要将 `counts[i] -= 1`。

## 3. 动画演示

![](https://www.runoob.com/wp-content/uploads/2019/03/countingSort.gif)

## 4. 算法分析

- 当输入元素是 `n` 个 `0 ~ k` 之间的整数时，计数排序的时间复杂度为 $O(n + k)$。
- 由于用于计数的数组 `counts` 的长度取决于待排序数组中数据的范围（等于待排序数组最大值减去最小值再加 `1`）。所以计数排序对于数据范围很大的数组，需要大量的时间和内存。
- 计数排序一般用于排序整数，不适用于按字母顺序排序人名。
- 计数排序是 **稳定排序算法**。

## 5. 代码实现

```Python
def countingSort(arr):
    arr_min, arr_max = min(arr), max(arr)
    size = arr_max - arr_min + 1
    counts = [0 for _ in range(size)]
    
    for num in arr:
        c[num - arr_min] += 1
    for j in range(1, size):
        counts[j] += counts[j - 1]
    
    res = [0 for _ in range(len(arr))]
    for i in range(len(arr) - 1, -1, -1):
        res[counts[arr[i] - arr_min] - 1] = arr[i]
        counts[arr[i] - arr_min] -= 1
    
    return res  
```

