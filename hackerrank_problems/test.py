from collections import defaultdict

def longest_subarray_with_2_close_values():
    nums = [0, 1, 2, 1, 2, 3]
    count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(nums)):
        count[nums[right]] += 1
        print(count)
        while len(count) > 2 or (len(count) == 2 and abs(max(count) - min(count)) > 1):
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        
        print(count)
        max_len = max(max_len, right - left + 1)

    return max_len


longest_subarray_with_2_close_values()