import csv
import os

class ManejadorCSV:
    """Clase para importar, modificar y exportar archivos CSV usando csv.reader y csv.writer."""

    # Registro nuevo a agregar. Las claves deben coincidir con los encabezados del CSV.
    REGISTRO_MISSINGNO = {
        "file_name": "0000-MissingNo-.png",
        "label": "",
        "name": "MissingNo",
        "generation": "1",
        "Type 1": "Normal",
        "Type 2": "",
        "HP": "33",
        "Attack": "136",
        "Defense": "0",
        "Sp.Attack": "6",
        "Sp.Defense": "6",
        "Speed": "29",
        "shiny": "no",
    }

    def __init__(self, filepath: str):
        self.filepath = filepath

    def leer_datos(self):
        """Importa el CSV usando csv.reader y retorna encabezados y filas."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"No se encontró el archivo CSV: '{self.filepath}'")

        # newline='' es lo recomendado por el módulo csv; utf-8-sig tolera un BOM inicial
        with open(self.filepath, mode='r', encoding='utf-8-sig', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if header is None:
                raise ValueError(f"El archivo CSV está vacío: '{self.filepath}'")
            rows = [row for row in reader if row]  # ignora líneas totalmente vacías
        return header, rows

    def agregar_registro(self, header, rows, registro: dict):
        """Agrega un registro (dict) al final de rows, ordenado según el encabezado.

        Las columnas que no estén en el diccionario quedan vacías.
        """
        rows.append([registro.get(col, "") for col in header])
        return rows

    def modificar_y_guardar(self, nuevo_filepath: str):
        """Agrega el registro de MissingNo y guarda un nuevo CSV (el original no se toca)."""
        header, rows = self.leer_datos()

        # Modificación: agregar a MissingNo solo si todavía no existe
        existentes = {fila[0] for fila in rows if fila}
        if self.REGISTRO_MISSINGNO["file_name"] not in existentes:
            self.agregar_registro(header, rows, self.REGISTRO_MISSINGNO)

        with open(nuevo_filepath, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)

        print(f"Archivo CSV modificado guardado exitosamente en: '{nuevo_filepath}'")
        return nuevo_filepath