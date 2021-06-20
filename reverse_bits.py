class Solution:
    def reverseBits(self, n):
        n = bin(n)[2:]#convert to binary number
        n = '%32s' % n #add extra spacing
        n = n.replace(' ','0')#converting the space into zero
        return int(n[::-1],2) #printing the reverse integer value 