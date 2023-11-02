#Ejemplo de creacion Codigo Python

# Precisiona  Mayús+F10 para ejecutar o remplazar el codigo# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import filedialog

class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        root.title("Bloc de notas Simplificado ")

        self.text_widget = tk.Text(root, wrap='word')
        self.text_widget.pack(expand=1, fill='both')

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nuevo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Salir", command=root.quit)

    def new_file(self):
        self.root.title("Nuevo archivo - Bloc de notas simple")
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.root.title(f"{file_path} - Bloc de notas simple")
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(1.0, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    SimpleNotepad(root)
    root.mainloop()
