# Problem: Sorting the Sentence  - https://leetcode.com/problems/sorting-the-sentence/description/

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        sorted_words = [''] * len(s)

        for word in s:
            position = int(word[-1]) - 1 
            sorted_words[position] = word[:-1]  

        reconstructed_sentence = ' '.join(sorted_words)

        return reconstructed_sentence