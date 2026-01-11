#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start

import random

class RandomizedSet:

    def __init__(self):
        self.value_set = []

    def insert(self, val: int) -> bool:
        if val in self.value_set:
            return False
        else:
            self.value_set.insert(val)

    def remove(self, val: int) -> bool:
        if val not in self.value_set:
            return False
        else:
            self.value_set.remove(val)

    def getRandom(self) -> int:
        return self.value_set[random.randrange(len(self.value_set))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

