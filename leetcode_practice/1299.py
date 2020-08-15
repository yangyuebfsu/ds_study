***
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
***
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=len(arr)-2
        largest=arr[-1]
        while i>-1:
            temp=arr[i]
            arr[i]=largest
            largest=max(temp, largest)
            i=i-1
        arr[-1]=-1
        return arr
