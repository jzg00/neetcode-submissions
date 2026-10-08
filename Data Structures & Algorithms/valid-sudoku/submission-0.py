class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]

                if cur == '.':
                    continue

                if cur in row[r] or cur in col[c] or cur in box[(r // 3, c // 3)]:
                    return False
                
                row[r].add(cur)
                col[c].add(cur)
                box[(r // 3, c // 3)].add(cur)
        
        return True