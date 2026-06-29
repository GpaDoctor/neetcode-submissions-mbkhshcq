"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Step 1: Sort the meetings by their start times.
        # This allows us to check for overlaps linearly since any overlapping 
        # meetings will now be adjacent to each other in the list.
        intervals.sort(key=lambda i: i.start)

        # Step 2: Iterate through the sorted intervals starting from the second meeting.
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # The previous meeting
            i2 = intervals[i]      # The current meeting

            # Step 3: Check if the previous meeting ends after the current meeting starts.
            # If it does, there is a time conflict (overlap), so the person cannot attend all meetings.
            if i1.end > i2.start:
                return False
                
        # Step 4: If the loop finishes without finding any overlaps, all meetings are clear.
        return True
