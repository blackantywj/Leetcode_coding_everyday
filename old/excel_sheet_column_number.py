class Solution:
    def titleToNumber(self, x: str) -> int:
        z=dict((j,i+1) for i,j in enumerate(ascii_uppercase))
        l=len(x)
        s=0
        for u in x:
            s+=z[u]*((26)**(l-1))
            l=l-1
<<<<<<< HEAD
        return s
=======
        return s
>>>>>>> 192284b0e5bae3db598e96e0a4267b85cab9ace8
