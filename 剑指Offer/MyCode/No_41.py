'''
剑指 Offer 第41题 及其变体
leetcode 295. Find Median from Data Stream
leetcode 480. Sliding Window Median
'''

import heapq

class MedianFinder:
# leetcode 295. Find Median from Data Stream
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []     # 用最大堆存储数组中较小的一半数, small中所有数据小于large中的最小值
        self.large = []     # 用最小堆存储数组中较大的一半数, large中所有数据大于small中的最大值

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return ( -self.small[0] + self.large[0] ) / 2     # 不要忘记self.small里存的是负数，取出时要加负号
        else:
            return self.large[0]

