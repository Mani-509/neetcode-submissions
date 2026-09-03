class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scores = []
        for op in operations:
            if op == '+':
                s1 = scores[-1]
                s2 = scores[-2]
                scores.append(s1 + s2)
            elif op == 'D':
                s1 = scores[-1]
                scores.append(2 * s1)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
            print(scores)
        return sum(scores)
        