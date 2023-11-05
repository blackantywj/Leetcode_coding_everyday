class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Base cases:
        # If either of numbers is 0 then ans is 0
        # If either of numbers is 1 then ans is the other number (multiplication identity)
        if num1 == "0" or num2 == "0":
            return "0"
        elif num1 == "1":
            return num2
        elif num2 == "1":
            return num1
        
        # Create int array from each digit
        a = [int(x) for x in num1]
        b = [int(y) for y in num2]
        
        # Resultant product will have at most m + n digits
        c = [0 for _ in range(len(a) + len(b))]
        
        # Perform normal multiplication of 2 numbers
        for i in range(len(a)-1, -1, -1):
            k = len(c) - (len(a) - i - 1) - 1
            carry = 0
            for j in range(len(b)-1, -1, -1):
                x = (a[i] * b[j]) + carry + c[k]
                c[k] = x % 10
                carry = x // 10
                k -= 1
            c[k] = carry
            
        # Revert back to string array
        c = [str(x) for x in c]
        # Discard leading 0, if any
        if c[0] == "0":
            return ''.join(c[1:])
        else:
            return ''.join(c)