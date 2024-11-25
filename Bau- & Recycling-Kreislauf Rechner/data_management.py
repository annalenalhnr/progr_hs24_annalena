# Verwaltung von Eingabedaten (Material, Kosten, Menge, Recyclinganteil)

import pandas as pd

# Laden von Materialdaten aus der Datei
def load_data(file_path):
    return pd.read_csv(file_path)

# Speichert Daten in einer Datei
def save_data(data, file_path):
    data.to_csv(file_path, index=False)

# Fügt ein neues Material zur Datentabelle hinzu
def add_material(data, material_name, recycling_rate, cost_per_unit, quantity):
  
    new_data = {'Material': material_name, 'Recyclingrate': recycling_rate, 'Kosten pro Einheit': cost_per_unit, 'Menge': quantity}
    return data.append(new_data, ignore_index=True)