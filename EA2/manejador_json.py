import json
import os

"""Clase para importar, modificar y exportar archivos JSON usando json.load y json.dump."""
class ManejadorJSON:
    def __init__(self, filepath: str):
        self.filepath = filepath

    """Importa el JSON usando json.load."""
    def leer_datos(self):
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    """Modifica los datos y guarda un nuevo archivo JSON usando json.dump."""
    def modificar_y_guardar(self, nuevo_filepath: str):
        data = self.leer_datos()
        
        # Modificación: Dependiendo de si es una lista o un diccionario
        if isinstance(data, list) and len(data) > 0:
            # Actualizar un valor del primer elemento o diccionario
            if isinstance(data[0], dict):
                data[0]["status_modificado"] = "Actualizado_JSON"
        elif isinstance(data, dict):
            data["status_modificado"] = "Actualizado_JSON"

        # Guardar el resultado en un nuevo archivo JSON con formato legible (indent=4)
        with open(nuevo_filepath, mode='w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print(f"Archivo JSON modificado guardado exitosamente en: '{nuevo_filepath}'")
        return nuevo_filepath