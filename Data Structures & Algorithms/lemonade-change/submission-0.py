from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Track the number of $5 and $10 bills we currently hold.
        # We don't need to track $20 bills because we never use them for change.
        five, ten = 0, 0
        
        for b in bills:
            if b == 5:
                # Scenario 1: Customer pays with $5. No change needed.
                five += 1
                
            elif b == 10:
                # Scenario 2: Customer pays with $10. We must give $5 back.
                five, ten = five - 1, ten + 1
                
            elif ten > 0:
                # Scenario 3: Customer pays with $20, and we have a $10 bill.
                # Greedy choice: Prefer giving change as $10 + $5 to save $5 bills.
                five, ten = five - 1, ten - 1
                
            else:
                # Scenario 4: Customer pays with $20, but we have no $10 bills.
                # Our only alternative is to give three $5 bills back.
                five -= 3
            
            # Safety Check: If our $5 bill count drops below zero at any point,
            # it means we were unable to provide the required change.
            if five < 0:
                return False
                
        # If we successfully served every customer in line, return True.
        return True
