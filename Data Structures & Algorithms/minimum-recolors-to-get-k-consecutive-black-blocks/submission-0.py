class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Count 'W's in the initial window of size k
        current_w = blocks[:k].count('W')
        min_w = current_w

        # Slide the window across the rest of the string
        for i in range(k, len(blocks)):
            # Add the new character entering the window
            if blocks[i] == 'W':
                current_w += 1
            # Remove the old character leaving the window
            if blocks[i - k] == 'W':
                current_w -= 1

            # Track the minimum white blocks found
            min_w = min(min_w, current_w)

        return min_w