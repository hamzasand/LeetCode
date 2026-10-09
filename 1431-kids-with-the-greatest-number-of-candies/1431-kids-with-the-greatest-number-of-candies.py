class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        boolean_list = []
        for i in candies:
            if i + extraCandies >= max(candies):
                boolean_list.append(True)
            else:
                boolean_list.append(False)
        return boolean_list

        