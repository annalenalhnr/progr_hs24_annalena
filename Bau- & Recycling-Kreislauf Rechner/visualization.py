# Erstellung der Visualisierung

import matplotlib.pyplot as plt

#Erstellen eines Balkendiagramms
def plot_cost_distribution(data):
    data.plot(kind='bar', x='Material', y='Kosten pro Einheit')
    plt.title("Kostenverteilung pro Material")
    plt.show()

# Erstellen eines Kreisdiagram
def plot_recycling_rate_pie(data):
    recycling_data = data.grouby('Recyclingrate').sum()
    recycling_data.plot.pie(y='Menge', labels=recycling_data.index)
    plt.title("Recyclinganteil nach Material")