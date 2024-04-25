import customtkinter as tk
import webbrowser

def open_url():
    url = entry.get()
    webbrowser.open_new(url)


root = tk.CTk()
root.geometry('450x100')
root.title("External Web Browser")


entry = tk.CTkEntry(root, placeholder_text='Enter your link here', width=350)
entry.pack(pady=10)

button = tk.CTkButton(root, text="Open URL", command=open_url)
button.pack()

if __name__ == "__main__":
    root.mainloop()
