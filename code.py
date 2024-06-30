import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame, textvariable=self.board[i][j], width=3, font=('Arial', 18), justify='center', bd=2, relief='solid')
                entry.grid(row=i, column=j, padx=(5, 5 if (j + 1) % 3 else 15), pady=(5, 5 if (i + 1) % 3 else 15))

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku, font=('Arial', 14))
        solve_button.pack(pady=10)

    def is_valid(self, num, row, col):
        for i in range(9):
            if self.board[row][i].get() == num:
                return False
            if self.board[i][col].get() == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j].get() == num:
                    return False

        return True

    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j].get() == "":
                    return (i, j)
        return None

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True
        row, col = empty

        for num in map(str, range(1, 10)):
            if self.is_valid(num, row, col):
                self.board[row][col].set(num)
                if self.solve():
                    return True
                self.board[row][col].set("")
        
        return False

    def solve_sudoku(self):
        if not self.solve():
            messagebox.showinfo("Sudoku Solver", "No solution exists for this Sudoku puzzle.")
        else:
            messagebox.showinfo("Sudoku Solver", "Sudoku puzzle solved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    solver = SudokuSolver(root)
    root.mainloop()
