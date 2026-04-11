class KthLargest:
    # 1. This part SETS UP the robot
    def __init__(self, k: int, nums: List[int]):
        # __init__ just states the robot name, color, etc.

        # self is nametag

        # use kingdom analogy
        self.minHeap = nums
        self.k = k
        # line up the crowd who tries to enter
        heapq.heapify(self.minHeap)
        # if 10 ppl that is larger than kingdom can hold
        # kick the shortest ppl out
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        
    #  2. This part is a SKILL (Method)
    def add(self, val: int) -> int:
        # let a ppl in
        heapq.heappush(self.minHeap, val)
        # if len larger than kingdom can hold
        if len(self.minHeap) > self.k:
            # kick the shortest ppl out
            heapq.heappop(self.minHeap)
        # the current shortest, which is the kth largest
        return self.minHeap[0]
        
# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
