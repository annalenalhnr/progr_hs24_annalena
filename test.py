import customtkinter as ctk

def getEntry():
    eingabe = entry.get()
    print(eingabe)
    label_entry.configure(text=eingabe)


root = ctk.CTk()

root.geometry("800x600")

label = ctk.CTkLabel(master=root, text="Hello World", font=("arial", 18))
label.pack(pady=10)

entry = ctk.CTkLabel(master=root, width=200)
entry.pack(pady=10)

button = ctk.CTkButton(master=root, text="Click me", command=getEntry)
button.pack(pady=10)

label_entry = ctk.CTkLabel(master=root, text="", font=("Arial", 12))
label_entry.place(relx=0.0, rely=1.0, y=-10, anchor="sw")

root.mainloop()

print(helloa)

