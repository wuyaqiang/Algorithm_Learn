### 1. 最长公共子序列（返回最大长度）

参考链接：[<https://www.techiedelight.com/longest-common-subsequence/>](<https://www.techiedelight.com/longest-common-subsequence/>)

##### 普通递归算法：

```python
def LCS_length(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    # 如果x和y的最后一个字符相等
    if x[m-1] == y[n-1]:
        return LCS_length(x, y, m-1, n-1) + 1
    # 如果x和y的最后一个字符不相等
    return max(LCS_length(x, y, m, n-1), LCS_length(x, y, m-1, n))
```

（该方法计算大量重复子问题，最坏时间复杂度为O(2 * exp(m+n))）

##### top-down 方法：

```python
def LCS_length(x, y, m, n, lookup):
    if m == 0 or n == 0:
        return 0
    # 给当前输入创建一个唯一键值
    key = (m, n)
    # 如果当前子问题不在lookup表中，即第一次出现，就解决该子问题并存储到哈希表中
    if key not in lookup:
        if x[m-1] == y[n-1]:
            lookup[key] = LCS_length(x, y, m-1, n-1, lookup) + 1
        else:
            lookup[key] = max(LCS_length(x, y, m, n-1, lookup), LCS_length(x, y, m-1, n, lookup))
    return lookup[key]
```

（该方法时间复杂度为O(mn)，空间复杂度为O(mn)）

##### bottom-up 方法：

![1562722994756](/home/wuyaqiang/.config/Typora/typora-user-images/1562722994756.png)

```python
def LCS_length(x, y):
    m, n = len(x), len(y)
    # dp矩阵用于存储子问题的解，i行j列的值表示x[0 : i-1]和y[0 : j-1]的LCS长度
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

（该方法时间复杂度为O(mn)，空间复杂度为O(mn)）

### 2. 最长公共子序列（返回所有最长子序列）

参考链接：[<https://www.techiedelight.com/longest-common-subsequence-finding-lcs/>](<https://www.techiedelight.com/longest-common-subsequence-finding-lcs/>)



### 3. 最短公共超序列

参考链接：[<https://www.techiedelight.com/shortest-common-supersequence-introduction-scs-length/>](<https://www.techiedelight.com/shortest-common-supersequence-introduction-scs-length/>)

```python
def SCS_length(x, y):
    m, n = len(x), len(y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    # 初始化dp矩阵的第一行和第一列:
    dp[0] = [i for i in range(n+1)]
    for i in range(m+1):
        dp[i][0] = i
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
    return dp[m][n]
```



