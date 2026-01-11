#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

import itertools
# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        for shift in itertools.combinations(range(10), turnedOn):
            watch = 0
            for i in shift:
                watch |= 1 << i
            m = watch & 0b1111
            h = watch >> 4
            print(f'{h}:{m:02}')
        
# @lc code=end

