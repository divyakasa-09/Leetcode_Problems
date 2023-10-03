class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict= {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        total = 0
        prev_value = 0
        
        # Iterate through the Roman numeral string from right to left
        for char in s[::-1]:
            value = roman_dict[char]
            
            # If the current value is smaller than the previous value, it's a subtraction case
            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total
