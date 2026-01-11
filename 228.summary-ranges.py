#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        begin_num = None
        end_num = None
        range_strings = []
        for num in nums:
            if begin_num is None and end_num is None:
                # 数値の群が指定されていない場合
                begin_num = num
                end_num = num
                continue
            if end_num == num - 1:
                # 直前の数値の群と数値numが連続だった場合
                end_num = num
            else:
                if begin_num == end_num:
                    # 数値の群の数が1つだった場合
                    range_strings.append(str(begin_num))
                else:
                    # 数値の群の数が複数だった場合
                    range_strings.append(f"{begin_num}->{end_num}")
                begin_num = num
                end_num = num
        if begin_num is not None and end_num is not None:
            if begin_num == end_num:
                # 数値の群の数が1つだった場合
                range_strings.append(str(begin_num))
            else:
                # 数値の群の数が複数だった場合
                range_strings.append(f"{begin_num}->{end_num}")
        
        return range_strings
    
#反省
#end_numを作らずに、numが最後の要素であるかnumとその一つ前の要素との差が1でなければ
# range_stringsリストに要素を追加するようにすればよかった。
# @lc code=end

