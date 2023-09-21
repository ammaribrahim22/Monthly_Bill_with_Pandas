import tkinter as tk
from tkinter import ttk, filedialog
import csv


def load_csv_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)

                # Clear the existing treeview
                for item in tree.get_children():
                    tree.delete(item)

                # Insert data into the treeview
                for row in data:
                    tree.insert('', 'end', values=row)
        except Exception as e:
            result_label.config(text=f"An error occurred: {str(e)}")
    else:
        result_label.config(text="No file selected.")


app = tk.Tk()
app.title("CSV File Viewer")

load_button = tk.Button(app, text="Open CSV File", command=load_csv_data)
load_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

tree = ttk.Treeview(app, columns=('Column 1', 'Column 2', 'Column 3'))
tree.heading('#1', text='Column 1')
tree.heading('#2', text='Column 2')
tree.heading('#3', text='Column 3')
tree.pack()

app.mainloop()
