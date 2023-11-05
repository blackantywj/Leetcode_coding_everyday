class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=n
        s=0
        x=x//5
        s+=x
        while(x>=5):
            x=x//5
            s+=x
<<<<<<< HEAD
        return s
=======
        return s
>>>>>>> 192284b0e5bae3db598e96e0a4267b85cab9ace8
