# Berechnung von Materialkosten, Recyclinganteil, etc.

# Brechnung der Gesamtkosten
def calculate_total_cost(data):
    return (data['Kosten pro Quadratmeter'] * data['Menge']).sum()

# Brechnung des durschnittlichen Recyclinganteil
def calculate_total_recycling_rate(data):
    total_quantity = data['Menge'].sum()
    weighted_recycling = (data['Recyclingrate'] * data['Menge']).sum()
    return weighted_recycling / total_quantity if total_quantity > 0 else 0