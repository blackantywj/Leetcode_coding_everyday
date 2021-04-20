class Solution():
	def solve(self, board):
		if not any(board): return

		m, n = len(board), len(board[0])
		save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
		while save:
			i, j = save.pop()
			if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
				board[i][j] = 'S'
				save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

		board[:] = [['XO'[c == 'S'] for c in row] for row in board]
		print(board)
		return board
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if not board:
			return
		n, m = len(board), len(board[0])
		boardFilter = lambda (i, j): 0 <= i < n and 0 <= j < m and board[i][j] == 'O'
		queue = filter(boardFilter, [x for i in range(max(n, m)) for x in ((i, 0), (i, m - 1), (0, i), (n - 1, i))])
		while queue:
			x, y = queue.pop()
			board[x][y] = 'M'
			queue.extend(filter(boardFilter, [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))
		board[:] = [['XO'[x == 'M'] for x in row] for row in board]


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

cc = Solution()

cc.solve(board)