***
551. Student Attendance Record I
Easy

327

884

Add to List

Share
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
***

class Solution:
    def checkRecord(self, s: str) -> bool:
        if 'LLL' in s:
            return False
        stu_record = list(s)
        try:
            stu_record.remove('A')
        except:
            pass
        return  'A' not in stu_record