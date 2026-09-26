class StockSpanner:

    def __init__(self):
        self.s = []
        self.arr = []

    def next(self, price: int) -> int:
        while self.s and price >= self.arr[self.s[-1]]:
            self.s.pop()
        
        self.arr.append(price)
        
        if not self.s:
            res = len(self.arr)
        else:
            res = len(self.arr) - 1 - self.s[-1]

        self.s.append(len(self.arr) - 1)

        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)