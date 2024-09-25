from collections import defaultdict
from typing import List
import heapq

# Solution 1: Bucket Sort -> time complexity: O(NlogK)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Build the frequency hashmap
        freq_hashmap = defaultdict(int)
        for num in nums:
            freq_hashmap[num] += 1

        # Step 2: Initialize the bucket sort list correctly - Bucket Algorithm
        freq_list = [[] for _ in range(len(nums) + 1)]

        # Possible Mistake to avoid in future
        # freq_list = [[]] * (len(nums) + 1)  # Incorrect: Single list referenced multiple times

        # Step 3: Populate the bucket list with numbers based on their frequencies
        for n, freq in freq_hashmap.items():
            if freq>0:
                freq_list[freq].append(n)

        top_k_elements = []
        for nums_arr in reversed(freq_list):
            for num in nums_arr:
                top_k_elements.append(num)
                if len(top_k_elements) == k:
                    return top_k_elements


# Solution 2: Using a heap -> time complexity: O(NlogK)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find the top K frequent elements in the given list of integers.

        :param nums: List of integers.
        :param k: Number of top frequent elements to return.
        :return: List of top k frequent elements.
        """
        # Step 1: Build the frequency hashmap
        num_freq_hashmap = defaultdict(int)
        for num in nums: # time complexity -> O(N)
            num_freq_hashmap[num] += 1

        # Step 2: Use a heap to find the top K frequent elements
        # We use a min-heap of size k
        min_heap = []
        for num, freq in num_freq_hashmap.items():
            # Push (freq, num) into the heap.
            # The heap orders by 'freq' first because freq is the first element in the tuple.
            heapq.heappush(min_heap, (freq, num)) # time complexity -> O(logK)

            # If the heap size exceeds k, remove the smallest element
            # This maintains the heap size to k containing the most frequent elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract the numbers from the heap
        # We get the top k frequent elements by extracting second element from each tuple in the heap
        top_k_frequent = [num for freq, num in min_heap]
        return top_k_frequent

# Solution 3: Using a heap -> time complexity: O(NlogK)
class Solution:
    @staticmethod
    def sort_dict_by_value(hashmap, dsc=False):
        # Sort the dictionary by value and return as a new dictionary
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=dsc)
        return {k: v for k, v in sorted_items}

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq_hashmap = defaultdict(int)
        for num in nums:
            num_freq_hashmap[num] += 1

        sorted_by_values = Solution.sort_dict_by_value(num_freq_hashmap, dsc=True)
        return list(sorted_by_values.keys())[:k]

