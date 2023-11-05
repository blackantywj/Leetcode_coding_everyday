# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         # fast sort
#         nums = nums1 + nums2
#         # print(nums)
#         high = len(nums)-1
#         resultlist = self.quickSort(nums, 0, high)
#         mid = int(len(resultlist) /2)
#         if len(nums) % 2 == 0:
#             print((nums[mid] + nums[mid-1]) /2)
#             return (nums[mid] + nums[mid-1]) /2
#         else:
#             print(nums[mid])
#             return (nums[mid])
        
#     def partition(self, arr,low,high): 
#         i = ( low-1 )        
#         pivot = arr[high]     

#         for j in range(low , high): 
#             if   arr[j] <= pivot: 

#                 i = i+1 
#                 arr[i],arr[j] = arr[j],arr[i] 

#         arr[i+1],arr[high] = arr[high],arr[i+1] 
#         return i+1 
    
#     def quickSort(self, arr, low, high): 
#         if low < high: 

#             pi = self.partition(arr,low,high) 

#             self.quickSort(arr, low, pi-1) 
#             self.quickSort(arr, pi+1, high)
#         return arr
A = [1, 2]
B = [3, 4]

# cc = Solution()

# cc.findMedianSortedArrays(nums1, nums2)
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = int((imin + imax) / 2)
        j = int(half_len - i)
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
print(median(A, B))