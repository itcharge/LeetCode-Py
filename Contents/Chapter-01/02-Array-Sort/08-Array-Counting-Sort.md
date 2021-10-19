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



## 5. 代码实现

```Python
def countingSort(arr):
    arr_min = min(arr)
    arr_max = max(arr)
    size = arr_max - arr_min + 1
    counts = [0 for _ in range(size)]
    
    for i in arr:
        c[i - arr_min] += 1
    for i in range(1, size):
        counts[i] = counts[i ]
        
```

