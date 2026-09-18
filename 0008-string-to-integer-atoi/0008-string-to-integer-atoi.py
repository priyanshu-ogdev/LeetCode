class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
            
        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            
            if sign == 1 and result > INT_MAX:
                return INT_MAX
            if sign == -1 and -result < INT_MIN:
                return INT_MIN
                
            index += 1
            
        return sign * result