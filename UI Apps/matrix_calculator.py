import tkinter as tk
from tkinter import messagebox
import numpy as np


def open_matrix_window():
    win = tk.Toplevel()
    win.title("Matrix Calculator (2x2)")
    win.geometry("400x350")

    tk.Label(win, text="Matrix A (2x2)").grid(row=0, column=0, columnspan=2, pady=5)
    tk.Label(win, text="Matrix B (2x2)").grid(row=0, column=2, columnspan=2, pady=5)

    a_entries = []
    b_entries = []

    for i in range(2):
        row_a = []
        row_b = []
        for j in range(2):
            e_a = tk.Entry(win, width=5)
            e_a.grid(row=i + 1, column=j, padx=5, pady=5)
            row_a.append(e_a)

            e_b = tk.Entry(win, width=5)
            e_b.grid(row=i + 1, column=j + 2, padx=5, pady=5)
            row_b.append(e_b)

        a_entries.append(row_a)
        b_entries.append(row_b)

    result_label = tk.Label(win, text="Result will appear here", font=("Arial", 10))
    result_label.grid(row=5, column=0, columnspan=4, pady=10)

    def get_matrices():
        try:
            A = np.array([[float(a_entries[i][j].get()) for j in range(2)] for i in range(2)])
            B = np.array([[float(b_entries[i][j].get()) for j in range(2)] for i in range(2)])
            return A, B
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return None, None

    def do_add():
        A, B = get_matrices()
        if A is None:
            return
        C = A + B
        result_label.config(text=f"Addition:\n{C}")

    def do_sub():
        A, B = get_matrices()
        if A is None:
            return
        C = A - B
        result_label.config(text=f"Subtraction:\n{C}")

    def do_mul():
        A, B = get_matrices()
        if A is None:
            return
        C = A @ B
        result_label.config(text=f"Multiplication:\n{C}")

    tk.Button(win, text="A + B", width=10, command=do_add).grid(row=3, column=0, columnspan=1, pady=10)
    tk.Button(win, text="A - B", width=10, command=do_sub).grid(row=3, column=1, columnspan=1, pady=10)
    tk.Button(win, text="A × B", width=10, command=do_mul).grid(row=3, column=2, columnspan=2, pady=10)
