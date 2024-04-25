import customtkinter as tk
import webbrowser
from tkinter import messagebox

def open_url():
    url = entry.get().strip()
    if url:
        try:
            webbrowser.open_new(url)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open URL: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter a valid URL")

root = tk.CTk()
root.geometry('450x100')
root.title("External Web Browser")

entry = tk.CTkEntry(root, width=350, placeholder_text='Enter your link here: ')
entry.pack(pady=10)

button = tk.CTkButton(root, text="Open URL", command=open_url)
button.pack()

if __name__ == "__main__":
    root.mainloop()
