## 1. 算法思想

> 快速排序（Quick Sort）基本思想：
>
> 通过一趟排序将无序序列分为独立的两个序列，第一个序列的值均比第二个序列的值小。然后递归地排列两个子序列，以达到整个序列有序。

## 2. 算法步骤

- 从数组中找到一个基准数。
- 然后将数组中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧，从而把数组拆分为左右两个部分。
- 再对左右两个部分分别重复第二步，直到各个部分只有一个数，则排序结束。

## 3. 动画演示

![](https://www.runoob.com/wp-content/uploads/2019/03/quickSort.gif)

## 4. 算法分析

- 在参加排序的元素初始时已经有序的情况下，快速排序方法花费的时间最长。此时，第 `1` 趟排序经过 `n - 1` 次比较以后，将第 `1` 个元素仍然确定在原来的位置上，并得到 `1` 个长度为 `n - 1` 的子序列；第 `2` 趟排序进过 `n - 2` 次比较以后，将第 `2` 个元素确定在它原来的位置上，又得到 `1` 个长度为 `n - 2` 的子序列；依次类推，最终总的比较次数为 $(n − 1) + (n − 2) + … + 1 = \frac{n(n − 1)}{2}$。因此时间复杂度为 $O(n^2)$。

- 还有一种情况，若每趟排序后，分界元素正好定位在序列的中间，从而把当前参加排序的序列分成大小相等的前后两个子序列，则对长度为 n 的序列进行快速排序所需要的时间为：

  $\begin{align}T(n) \le & \ n + 2T(n/2) \\ \le & \ 2n + 4T(n/2) \\ \le & \ 3n + 8T(n/8) \\ & …… \\ \le & \ (log_2 n)n + nT(1) = O(nlog_2 n) \end{align}$

  因此，快速排序方法的时间复杂度为 $O(nlog_2 n)$，时间性能显然优于前面讨论的几种排序算法。

- 无论快速排序算法递归与否，排序过程中都需要用到堆栈或其他结构的辅助空间来存放当前待排序序列的首、尾位置。最坏的情况下，空间复杂度为 $O(n)$。

- 若对算法进行一些改写，在一趟排序之后比较被划分所得到的两个子序列的长度，并且首先对长度较短的子序列进行快速排序，这时候需要的空间复杂度可以达到 $O(log_2 n)$。

- 快速排序时一种 **不稳定排序算法**，也是一种不适合在链表结构上实现的排序算法。

## 5. 代码实现

```Python
import random

def randomPartition(arr: [int], low: int, high: int):
		i = random.randint(low, high)
		arr[i], arr[high] = arr[high], arr[i]
		return partition(arr, low, high)

def partition(arr: [int], low: int, high: int):
	x = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= arr[high]:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

def quickSort(arr, low, high):
	n = len(arr)
	if low < high:
		pi = randomPartition(arr, low, high)
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)

	return arr
```

