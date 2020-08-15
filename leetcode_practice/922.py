***
922. Sort Array By Parity II

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

***

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i=0
        should_be_odd=[]
        should_be_even=[]
        while i<len(A):
            if (i%2==0)&(A[i]%2!=0):
                should_be_even.append(i)
            elif (i%2!=0)&(A[i]%2==0):
                should_be_odd.append(i)
            else:
                pass
            i+=1
        for x in range( len(should_be_odd) ):
            A[should_be_odd[x]], A[should_be_even[x]] = A[should_be_even[x]],A[should_be_odd[x]]
        return A
