#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citation_list = [0] * (len(citations) + 1)
        for citation in citations:
            citation_list[min(len(citations), citation)] += 1
        
        cul_citation = 0
        for i in range(len(citation), -1, -1):
            cul_citation += citation_list[i]
            if cul_citation >= i:
                return len(citation) - i + 1
        
        return 0
# @lc code=end

