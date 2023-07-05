from typing import List
import heapq

from record import Record


class UserAgent:
    def __init__(self, id: int):
        self.id: int = id
        self.records: List[Record] = []

    def add_record(self, record: Record):
        heapq.heappush(self.records, record)
