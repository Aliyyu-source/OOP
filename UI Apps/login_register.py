from tkinter import *
from tkinter import messagebox

# Correct login credentials
USERNAME = "Madhusudan"
PASSWORD = "Regmi"

# ---------------------------------------------------------
# MAIN MENU WINDOW (SECOND WINDOW)
# ---------------------------------------------------------
def open_main_menu():
    menu = Toplevel()
    menu.title("LAB NumPy Project - Main Menu")
    menu.geometry("400x350")
    menu.config(bg="#f0f0f0")

    Label(menu, text="LAB NumPy Project", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    # ⭐ Lazy imports (fixes circular imports and removes blank Tk window)
    def open_matrix():
        from matrix_calculator import open_matrix_window
        open_matrix_window()

    def open_square():
        from rotate_square import run
        run()

    def open_cube():
        from rotate_cube import run
        run()

    def open_rockets():
        from rockets import run
        run()

    Button(menu, text="Matrix Calculator", width=25,
           command=open_matrix,
           bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=5)

    Button(menu, text="Rotate Square in 3D", width=25,
           command=open_square,
           bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=5)

    Button(menu, text="Rotate Cube in 3D", width=25,
           command=open_cube,
           bg="#FF9800", fg="white", font=("Arial", 11)).pack(pady=5)

    Button(menu, text="2 Rockets Flying to the Moon", width=25,
           command=open_rockets,
           bg="#9C27B0", fg="white", font=("Arial", 11)).pack(pady=5)

    Button(menu, text="Register", width=25,
           command=open_register_window,
           bg="#03A9F4", fg="white", font=("Arial", 11)).pack(pady=5)

    Button(menu, text="Exit", width=25,
           command=menu.destroy,
           bg="#f44336", fg="white", font=("Arial", 11)).pack(pady=15)


# ---------------------------------------------------------
# REGISTER WINDOW
# ---------------------------------------------------------
def open_register_window():
    reg = Toplevel()
    reg.title("Register")
    reg.geometry("300x220")
    reg.config(bg="#f0f0f0")

    Label(reg, text="New Username", bg="#f0f0f0").pack(pady=5)
    user = Entry(reg)
    user.pack()

    Label(reg, text="New Password", bg="#f0f0f0").pack(pady=5)
    pwd = Entry(reg, show="*")
    pwd.pack()

    Label(reg, text="Confirm Password", bg="#f0f0f0").pack(pady=5)
    confirm = Entry(reg, show="*")
    confirm.pack()

    def register_user():
        if pwd.get() != confirm.get():
            messagebox.showerror("Error", "Passwords do not match")
        else:
            messagebox.showinfo("Success", "Registration successful")
            reg.destroy()

    Button(reg, text="Register", bg="#4CAF50", fg="white",
           command=register_user).pack(pady=10)


# ---------------------------------------------------------
# LOGIN WINDOW (FIRST WINDOW)
# ---------------------------------------------------------
def open_login_window():
    login = Tk()   # ONLY Tk() IN THE WHOLE APP
    login.title("Login")
    login.geometry("300x200")
    login.config(bg="#f0f0f0")

    Label(login, text="Username", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    username_entry = Entry(login, font=("Arial", 12))
    username_entry.pack()

    Label(login, text="Password", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    password_entry = Entry(login, show="*", font=("Arial", 12))
    password_entry.pack()

    error_label = Label(login, text="", bg="#f0f0f0", fg="red")
    error_label.pack()

    def check_login():
        if username_entry.get() == USERNAME and password_entry.get() == PASSWORD:
            login.destroy()
            open_main_menu()
        else:
            error_label.config(text="Incorrect username or password")

    Button(login, text="Login", bg="#4CAF50", fg="white",
           font=("Arial", 12), command=check_login).pack(pady=10)

    login.mainloop()
