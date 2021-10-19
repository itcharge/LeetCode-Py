## 1. 算法思想

> 归并排序（Merge Sort）基本思想：
>
> 将两个或者多个有序序列合并成一个有序序列。

## 2. 算法步骤

- 初始时，将待排序序列中的 `n` 个记录看成 `n` 个有序子序列（每个子序列总是有序的），每个子序列的长度均为 `1`。
- 把当前序列组中有序子序列两两归并，完成一遍之后序列组里的排序序列个数减半，每个子序列的长度加倍。
- 对长度加倍的有序子序列重复上面的操作，最终得到一个长度为 `n` 的有序序列。

## 3. 动画演示

![](https://www.runoob.com/wp-content/uploads/2019/03/mergeSort.gif)

## 4. 算法分析

- 归并排序算法的时间复杂度等于归并趟数与每一趟归并的时间复杂度成绩。子算法 `merge(left_arr, right_arr):` 的时间复杂度是 $O(n)$，因此，归并排序算法总的时间复杂度为 $O(nlog_2n)$。
- 归并排序方法需要用到与参加排序的序列同样大小的辅助空间。因此算法的空间复杂度为 $O(n)$。
- 因为在两个有序子序列的归并过程中，如果两个有序序列中出现相同元素，`merge(left_arr, right_arr):` 算法能够使前一个序列中那个相同元素先被复制，从而确保这两个元素的相对次序不发生改变。所以归并排序算法是 **稳定排序算法**。

## 5. 代码实现

```Python
def merge(left_arr, right_arr):
    arr = []
    while left_arr and right_arr:
        if left_arr[0] <= right_arr[0]:
            arr.append(left_arr.pop(0))
        else:
            arr.append(right_arr.pop(0))
    while left_arr:
        arr.append(left_arr.pop(0))
    while right_arr:
        arr.append(right_arr.pop(0))
    return arr

def mergeSort(arr):
	size = len(arr)
    if size < 2:
        return arr
   	mid = len(arr) // 2
    left_arr, right_arr = arr[0: mid], arr[mid:]
    return merge(mergeSort(left_arr), mergeSort(right_arr))
```

