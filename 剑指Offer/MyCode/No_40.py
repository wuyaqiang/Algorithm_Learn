'''
剑指 Offer 第40题 最小的k个数
'''

import heapq

def smallest_k(nums, k):
    # heapq.heapify(nums)
    return heapq.nsmallest(k, nums)

if __name__ == '__main__':

    print(smallest_k([4,5,1,6,2,7,3,8], 4))