class Record:
    def __init__(self, start_timestamp, end_timestamp):
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp

    def __lt__(self, other):
        return self.start_timestamp < other.start_timestamp
