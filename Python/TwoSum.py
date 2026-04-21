# Bài toán 1: Algorithm (Tư duy xử lý mảng)
# Tên bài: Tìm cặp chỉ số có tổng bằng Target.

# Input: * Một mảng số nguyên nums (ví dụ: [2, 7, 11, 15]).

# Một số nguyên target (ví dụ: 9).

# Output: * Mảng chứa 2 chỉ số của 2 số có tổng bằng target. Ví dụ: [0, 1].

# Ràng buộc: O(n) thời gian 

# Problem: https://leetcode.com/problems/two-sum/

## Solve: Sử dụng hashmap để lưu trữ key value, nếu giá trị đang tính
# x + y = target -> có x, target rồi cần tìm y -> y = target - x là xong
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}

        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num in num_dict:
                return [i, num_dict[second_num]]
            num_dict[nums[i]] = i
        return None