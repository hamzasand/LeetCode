
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        left = [1] * n
        right = [1] * n
        answer = [1] * n

        # Calculate products on the left
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Calculate products on the right
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Combine left and right products
        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer
