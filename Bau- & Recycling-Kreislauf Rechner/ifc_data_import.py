# Materialdaten extrahieren

import ifcopenshell

def extract_materials_from_ifc(file_path):
    ifc_file = ifcopenshell.open(file_path)
    materials = []
    for product in ifc_file.by_type("IfcProduct"):
        materials.append({
            'Material': product.Name,
            'Menge': product.Quantity,
        })
    return materials