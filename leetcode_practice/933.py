***
933. Number of Recent Calls

Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

 

Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
***

class RecentCounter:

    def __init__(self):
        self.record=[]
        

    def ping(self, t: int) -> int:
        self.record.append(t)
        output=[]
        i=len(self.record)-1
        while i>=0:
            if self.record[i]>=t-3000:
                output.append(i)
            else:
                break
            i=i-1
        return len(output)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


#deque with popleft is more suitable for this tasks
import collections
class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)
