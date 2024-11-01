from sudokus_solver import sudokus_solver


sudoku = [
    [4, 0, 9, 1, 0, 5, 0, 0, 6],
    [0, 0, 1, 0, 7, 4, 9, 8, 2],
    [3, 0, 0, 0, 0, 2, 0, 0, 1],
    [9, 0, 0, 5, 3, 0, 6, 2, 0],
    [0, 5, 0, 0, 0, 9, 0, 1, 0],
    [0, 0, 3, 8, 2, 7, 0, 0, 0],
    [8, 3, 2, 4, 0, 6, 1, 7, 5],
    [0, 0, 0, 0, 1, 8, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 2, 0, 0]
]


# Crear una instancia del solucionador y resolver el Sudoku
solver = sudokus_solver(sudoku)
solved_sudoku = solver.solve()

# Imprimir el Sudoku resuelto
print("Sudoku resuelto:")
print(solved_sudoku)


import tkinter as tk
from tkinter import messagebox
from sudokus_solver import sudokus_solver  

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        
        # Crear una matriz de celdas de entrada para el sudoku
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        
        # Crear la cuadrícula de entrada
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = entry

        # Botón para resolver el sudoku
        solve_button = tk.Button(root, text="Resolver", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    def get_sudoku_from_entries(self):
        """Obtener el sudoku ingresado en la interfaz como una matriz 9x9"""
        sudoku = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit() and 1 <= int(value) <= 9:
                    row.append(int(value))
                else:
                    row.append(0)
            sudoku.append(row)
        return sudoku

    def display_solution(self, solution):
        """Mostrar la solución en la interfaz"""
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, solution[i][j])

    def solve(self):
        """Intentar resolver el sudoku ingresado"""
        sudoku = self.get_sudoku_from_entries()
        solver = sudokus_solver(sudoku)
        solution = solver.solve()
        
        # Comprobar si se encontró una solución
        if solution is not None:
            self.display_solution(solution)
        else:
            messagebox.showerror("Error", "No se pudo encontrar una solución para el sudoku ingresado")

root = tk.Tk()
gui = SudokuGUI(root)
root.mainloop()
