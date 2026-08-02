class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mac = []
        for op in operations:
            if op == "+":
                # Add the last two scores in the record
                mac.append(mac[-1] + mac[-2])
            elif op == "C":
                # Remove the last score from the record
                mac.pop()
            elif op == "D":
                # Double the last score
                mac.append(mac[-1] * 2)
            else:
                # Convert the string to an integer and record it
                mac.append(int(op))
                
        return sum(mac)