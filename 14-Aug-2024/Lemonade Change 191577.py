# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_count = ten_count = 0

        for bill in bills:
            if bill == 5:
                five_count += 1
            elif bill == 10:
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1
            else:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False

        return True

        