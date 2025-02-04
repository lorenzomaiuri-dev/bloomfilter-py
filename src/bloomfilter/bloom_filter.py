import hashlib
import math
from bitarray import bitarray
from typing import List

class BloomFilter:
    """
    A probabilistic data structure for membership testing.
    It allows false positives but never false negatives.
    
    Attributes:
        size (int): Number of bits in the filter.
        hash_count (int): Number of hash functions.
        bit_array (bitarray): Bit array storing the elements.
    """

    
    def __init__(self, expected_items: int, false_positive_rate: float):
        """
        Initializes the Bloom Filter with optimal size and hash functions.
        
        Args:
            expected_items (int): Estimated number of elements to store.
            false_positive_rate (float): Desired false positive probability.
        """

        self.size = self._optimal_size(expected_items, false_positive_rate)
        self.hash_count = self._optimal_hash_count(self.size, expected_items)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
    

    def _hashes(self, item: str) -> List[int]:
        """Generates multiple hash values for an item."""

        return [int(hashlib.md5((item + str(i)).encode()).hexdigest(), 16) % self.size for i in range(self.hash_count)]
    

    def add(self, item: str) -> None:
        """Adds an item to the Bloom Filter."""

        for index in self._hashes(item):
            self.bit_array[index] = 1
    

    def check(self, item: str) -> bool:
        """Checks if an item might be in the Bloom Filter."""

        return all(self.bit_array[index] for index in self._hashes(item))
    

    @staticmethod
    def _optimal_size(n: int, p: float) -> int:
        """Computes the optimal bit array size."""

        return int(-(n * math.log(p)) / (math.log(2) ** 2))
    

    @staticmethod
    def _optimal_hash_count(m: int, n: int) -> int:
        """Computes the optimal number of hash functions."""

        return int((m / n) * math.log(2))
