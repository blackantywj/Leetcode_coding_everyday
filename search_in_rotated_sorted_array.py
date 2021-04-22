def search(self, nums, target):
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) / 2
            
            if (nums[mid] < nums[0]) == ( target < nums[0]):
                if (nums[mid] < target):
                    lo = mid + 1
                elif (nums[mid] > target):
                    hi = mid
                else:
                    return mid
            elif target < nums[0]:
                lo = mid + 1
            else:
                hi = mid

        return -1
# 和第一个点比较，缩小查找空间直到找到那个节点