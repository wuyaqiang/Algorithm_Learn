
def quick_sort(nums):

    def sort(nums, l, r):

        if l >= r:
            return

        x = nums[l]
        i, j = l, r
        while i < j:

            while i < j and nums[j] > x:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] <= x:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1

        nums[i] = x
        sort(nums, l, i - 1)
        sort(nums, i + 1, r)

    sort(nums, 0, len(nums) - 1)

    return nums

if __name__ == "__main__":

    print(quick_sort([72, 6, 57, 88, 60, 42, 83, 73, 48, 85]))