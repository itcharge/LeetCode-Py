比如说写一个算法，计算 1~n 整数的和。

先来看第一种算法：

```Python
def sum(n):
    sum = 0
	num = 1
    while num <= n:
    	sum += num
        num += 1
	return sum
```

再来看第二种算法：

```Python
def sum(n):
    sum = (1 + n) * n / 2
    return sum
```

第一种算法要完成题目要求，需要定义两个变量 num、sum，并执行 100 次加法计算。而第二种方法需要定义一个变量  sum，并执行一次加法运算，一次乘法运算，一次除法运算。