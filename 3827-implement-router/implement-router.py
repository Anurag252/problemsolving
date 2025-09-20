from collections import deque, defaultdict
from typing import List
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()  # store packets as (source, destination, timestamp)
        self.hs = set()   # track unique packets
        self.memory = memoryLimit
        self.dst_map = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.hs:
            return False
        self.hs.add(packet)

        # Remove oldest if memory full
        if len(self.q) == self.memory:
            old = self.q.popleft()
            self.hs.remove(old)
            # Remove old timestamp from destination map
            old_dest = old[1]
            self.dst_map[old_dest].pop(0)

        # Add new packet
        self.q.append(packet)
        self.dst_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        t = self.q.popleft()
        self.hs.remove(t)
        self.dst_map[t[1]].pop(0)
        return list(t)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dst_map.get(destination, [])
        l = bisect_left(timestamps, startTime)
        r = bisect_right(timestamps, endTime)
        return r - l
