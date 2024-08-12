# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]): 
        self.history = []
        self.end_time = times[-1]
        self.n = len(times)
        cnt = Counter()
        max_votes = 0
        lead_person = None
        for i,time in enumerate(times):
            save = cnt[persons[i]] + 1
            cnt[persons[i]] = save 
            if save >= max_votes : 
                lead_person = persons[i]
                max_votes = save

            self.history.append((time,lead_person))
        print(self.history)


    def q(self, t: int) -> int:
        if t >= self.end_time : 
            return self.history[-1][1]
        
        i = bisect_right(self.history,t,key=lambda x:x[0])
        if i == 0 :
            return 0
        return self.history[i-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)