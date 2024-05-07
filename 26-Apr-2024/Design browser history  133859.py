# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_idx = 0

    def visit(self, url: str) -> None:
        self.curr_idx += 1
        if self.curr_idx < len(self.history):
            self.history = self.history[:self.curr_idx]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.curr_idx = max(0, self.curr_idx - steps)
        return self.history[self.curr_idx]

    def forward(self, steps: int) -> str:
        self.curr_idx = min(len(self.history) - 1, self.curr_idx + steps)
        return self.history[self.curr_idx]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)