# Benutzeroberfläche erstellen

import tkinter as tk
from tkinter import filedialog
from data_management import add_material, load_data, save_data
from calculations import calculate_total_cost, calculate_total_recycling_rate
from visualization import plot_cost_distribution, plot_recycling_rate_pie

def run_interface():
    root = tk.Tk()
    root.title("Bau- & Recycling-Kreislauf Rechner")

    # Eingabefelder
    tk.Label(root, text="Materialname"). grid(row=0)
    material_name_entry = tk.Entry(root)
    material_name_entry.grid(row=0, column=1)

    # Weitere EIngabefelder
    tk.Button(root, text="Kostenverteilung anzeigen", command=plot_cost_distribution).grid(row=3, column=0)
    tk.Button(root, text="Recyclinganteil anzeigen", command=plot_recycling_rate_pie).grid(row=3, column=1)

    root.mainloop()