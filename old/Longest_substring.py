class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = []
        record = 0
        for i, element in enumerate(s):
            if element not in dic:
                dic.append(element)
            elif element == dic[0]:
                dic.remove(dic[0])
                dic.append(element)
            elif element != dic[0]:   
                dic = dic[dic.index(element)+1:]
                dic.append(element)
            if record < len(dic):
                record = len(dic)
        print(record)
        return record

s='abcabgcbaywssb'
cc = Solution()

cc.lengthOfLongestSubstring(s)