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
>>>>>>> f8e7c831407587f60a104ad002a5eca3aef9ec7d
