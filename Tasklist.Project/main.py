from tkinter import *
import sqlite3


# ---------------------------------------------------------
# FUNCTION TO OPEN MAIN APP AFTER LOGIN
# ---------------------------------------------------------

def open_main_app():

    # ---------------------------------------------------------
    # DATABASE SETUP
    # ---------------------------------------------------------
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task TEXT
        )
    """)

    conn.commit()
    conn.close()

    # ---------------------------------------------------------
    # MAIN WINDOW SETUP
    # ---------------------------------------------------------
    root = Toplevel()
    root.title("My_Tasklist_App")
    root.geometry("400x450")
    root.config(bg="#f0f0f0")

    # Bring main window to front
    root.lift()
    root.attributes('-topmost', True)
    root.after(100, lambda: root.attributes('-topmost', False))

    # ---------------------------------------------------------
    # FUNCTIONS
    # ---------------------------------------------------------

    def submit():
        task_text = task.get().strip()

        if task_text == "":
            return

        conn = sqlite3.connect("tasklist.db")
        c = conn.cursor()

        c.execute("INSERT INTO tasks VALUES (:task)", {'task': task_text})

        conn.commit()
        conn.close()

        task.delete(0, END)

    def query():
        conn = sqlite3.connect("tasklist.db")
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM tasks")
        records = c.fetchall()

        task_listbox.delete(0, END)

        for record in records:
            task_listbox.insert(END, f"{record[0]} - {record[1]}")

        conn.close()

    def delete():
        conn = sqlite3.connect("tasklist.db")
        c = conn.cursor()

        c.execute("DELETE FROM tasks WHERE rowid = :id",
                  {'id': delete_box.get()})

        conn.commit()
        conn.close()

        delete_box.delete(0, END)

    def edit():
        global editor
        editor = Tk()
        editor.title("Muokkaa tehtävää")
        editor.geometry("400x200")

        conn = sqlite3.connect("tasklist.db")
        c = conn.cursor()

        task_id = delete_box.get()

        c.execute("SELECT * FROM tasks WHERE rowid = :id", {'id': task_id})
        record = c.fetchone()

        conn.close()

        edit_label = Label(editor, text="Muokkaa tehtävää", font=("Arial", 12))
        edit_label.grid(row=0, column=0, pady=10)

        global edit_box
        edit_box = Entry(editor, width=30, font=("Arial", 12))
        edit_box.grid(row=1, column=0, padx=20)
        edit_box.insert(0, record[0])

        save_btn = Button(editor, text="Tallenna muutokset",
                          command=update,
                          bg="#4CAF50", fg="white", font=("Arial", 11))
        save_btn.grid(row=2, column=0, pady=10)

    def update():
        conn = sqlite3.connect("tasklist.db")
        c = conn.cursor()

        task_id = delete_box.get()

        c.execute("""UPDATE tasks SET
            task = :task
            WHERE rowid = :id""",
                  {'task': edit_box.get(), 'id': task_id})

        conn.commit()
        conn.close()

        editor.destroy()

    # ---------------------------------------------------------
    # GUI ELEMENTS
    # ---------------------------------------------------------

    task_label = Label(root, text="Tehtävä", bg="#f0f0f0", font=("Arial", 12))
    task_label.grid(row=0, column=0, pady=(10, 0))

    task = Entry(root, width=30, font=("Arial", 12))
    task.grid(row=0, column=1, padx=20, pady=(10, 0))

    submit_btn = Button(root, text="Lisää tehtävä tietokantaan",
                        command=submit,
                        bg="#4CAF50", fg="white", font=("Arial", 11))
    submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    query_btn = Button(root, text="Näytä tehtävät",
                       command=query,
                       bg="#2196F3", fg="white", font=("Arial", 11))
    query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

    select_label = Label(root, text="Valitse ID", bg="#f0f0f0", font=("Arial", 12))
    select_label.grid(row=4, column=0, pady=5)

    delete_box = Entry(root, width=30, font=("Arial", 12))
    delete_box.grid(row=4, column=1, pady=5)

    delete_btn = Button(root, text="Poista tehtävä",
                        command=delete,
                        bg="#f44336", fg="white", font=("Arial", 11))
    delete_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    edit_btn = Button(root, text="Muokkaa tehtävää",
                      command=edit,
                      bg="#FF9800", fg="white", font=("Arial", 11))
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    task_listbox = Listbox(root, width=40, height=10, font=("Arial", 12))
    task_listbox.grid(row=7, column=0, columnspan=2, pady=10)

    scrollbar = Scrollbar(root)
    scrollbar.grid(row=7, column=2, sticky='ns')

    task_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_listbox.yview)


# ---------------------------------------------------------
# LOGIN WINDOW
# ---------------------------------------------------------

login_window = Tk()
login_window.title("Login")
login_window.geometry("300x200")
login_window.config(bg="#f0f0f0")

Label(login_window, text="Username", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
username_entry = Entry(login_window, font=("Arial", 12))
username_entry.pack()

Label(login_window, text="Password", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
password_entry = Entry(login_window, show="*", font=("Arial", 12))
password_entry.pack()

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "012345":
        login_window.destroy()
        open_main_app()
    else:
        error_label.config(text="Incorrect username or password", fg="red")

Button(login_window, text="Login", command=check_login,
       bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

error_label = Label(login_window, text="", bg="#f0f0f0", font=("Arial", 10))
error_label.pack()

login_window.mainloop()