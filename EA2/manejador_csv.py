import csv
import os

"""Clase para importar, modificar y exportar archivos CSV usando csv.reader y csv.writer."""
class ManejadorCSV:
    def __init__(self, filepath: str):
        self.filepath = filepath

    """Importa el CSV usando csv.reader y retorna encabezados y filas."""
    def leer_datos(self):
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = [row for row in reader]
        return header, rows

    """Modifica los datos y guarda un nuevo archivo CSV."""
    def modificar_y_guardar(self, nuevo_filepath: str):
        header, rows = self.leer_datos()
        
        # Modificación 1: Agregar un registro nuevo o actualizar un valor
        if rows:
            # Modificar el primer valor de la primera fila
            rows[0][0] = "Modificado_CSV"
            
        # Guardar en un nuevo archivo CSV conservando el original
        with open(nuevo_filepath, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
            
        print(f"Archivo CSV modificado guardado exitosamente en: '{nuevo_filepath}'")
        return nuevo_filepath