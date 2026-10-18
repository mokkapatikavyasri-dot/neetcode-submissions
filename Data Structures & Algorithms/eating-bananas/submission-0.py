class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            # Calculate total hours required
            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                right = mid  # Try a smaller speed
            else:
                left = mid + 1  # Increase the speed

        return left