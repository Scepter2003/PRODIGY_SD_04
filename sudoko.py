import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")
        self.grid = [[0]*9 for _ in range(9)]
        self.entries = [[None]*9 for _ in range(9)]

        #GUI
        for i in range(9):
            for j in range(9):
                e = tk.Entry(self.window, width=4)
                e.grid(row=i, column=j)
                self.entries[i][j] = e

        #buttons
        solve_button = tk.Button(self.window, text="Solve", command=self.solve)
        solve_button.grid(row=12, column=0, columnspan=9)

        clear_button = tk.Button(self.window, text="Clear", command=self.clear)
        clear_button.grid(row=10, column=0, columnspan=9)

    def solve(self):
        # Get grid values from GUI
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val == "":
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = int(val)

        # Solve Sudoku puzzle
        if self.solve_sudoku(self.grid):
            # Display solved grid
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
        else:
            messagebox.showerror("Error", "No solution found")

    def clear(self):
        # Clear GUI
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)

    def solve_sudoku(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, i, j, num):
                            grid[i][j] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True

    def is_valid(self, grid, row, col, num):
        # Check row
        for x in range(9):
            if grid[row][x] == num:
                return False

        # Check column
        for x in range(9):
            if grid[x][col] == num:
                return False

        # Check box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    solver = SudokuSolver()
    solver.run()
