***
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

***

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output=[]
        i=left
        while i<right+1:
            digits=[int(x) for x in list(str(i))]
            if 0 in digits:
                pass
            else:
                if any([ i%digit!=0 for digit in digits]):
                    pass
                else:
                    output.append(i)
            i+=1
        return output
