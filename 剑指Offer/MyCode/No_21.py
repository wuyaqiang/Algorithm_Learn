'''
剑指 Offer 第21题 及其相似题
leetcode 905. Sort Array By Parity
leetcode 922. Sort Array By Parity II
leetcode 328. Odd Even Linked List
'''

def sort_array_by_parity(nums):
    '''
    剑指 Offer 第21题
    leetcode 905. Sort Array By Parity
    '''
    # 解法一：O(n)
    # if not nums or len(nums) == 0:
    #     return []
    # even_idx = 0
    # for idx, num in enumerate(nums):
    #     if num % 2 == 0:
    #         nums[even_idx], nums[idx] = nums[idx], nums[even_idx]
    #         even_idx += 1
    # return nums

    # 解法二：利用两个指针，分别从前往后和从后往前遍历，O(n)
    # if not nums or len(nums) == 0:
    #     return []
    # l, r = 0, len(nums) - 1
    # while l < r:
    #     if nums[l] % 2 == 0:
    #         l += 1
    #     else:
    #         nums[l], nums[r] = nums[r], nums[l]
    #         r -= 1
    # return nums

    # 解法三：直接自定义排序规则, 但是时间复杂度最大, O(nlogn)
    return sorted(nums, key = lambda x: x % 2)

def sort_array_by_parity_2(nums):
    '''
    leetcode 922. Sort Array By Parity II
    '''
    if not nums or len(nums) == 0:
        return []
    even_idx, odd_idx, length = 0, 1, len(nums)
    while even_idx < length and odd_idx < length:
        if nums[even_idx] % 2 == 0:
            even_idx += 2
        elif nums[odd_idx] % 2 == 1:
            odd_idx += 2
        else:
            nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            even_idx += 2
            odd_idx += 2
    return nums

def odd_even_linked_list(head):
    '''
    leetcode 328. Odd Even Linked List
    '''
    if not head or not head.next:
        return head

    odd_head, even_head = head, head.next
    odd, even = odd_head, even_head
    while even:
        odd.next = even.next
        if not even.next:
            even.next = None
            break
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head

    return odd_head
























