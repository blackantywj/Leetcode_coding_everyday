class Solution:
    '''
    My code like garbage
    '''
    def lengthOfLastWord(self, s: str) -> int:
        lists = list(s)
        # print(lists)
        count = 0
        flag = 0
        # lists = lists.reverse()
        # print(lists[::-1])
        for i in lists[::-1]:
            # if lists[0] == ' ':
            #     continue
            if lists[::-1][0] == ' ':
                flag == 1
            if i != ' ':
                count += 1
            elif i == ' ' and count != 0:
                break
        return count
    '''
    God code

    class Solution:
        def lengthOfLastWord(self, s):
            return len(s.rstrip(' ').split(' ')[-1])
    '''
s = 'a '

cc = Solution()

print(cc.lengthOfLastWord(s))