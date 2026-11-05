import json
import os

class ManejadorJSON:
    """Clase para importar, modificar y exportar archivos JSON usando json.load y json.dump."""

    CAMPO_ESTADO = "estado_revision"
    VALOR_ESTADO = "verificado_gen1_9"

    def __init__(self, filepath: str):
        self.filepath = filepath

    def leer_datos(self):
        """Importa el JSON usando json.load."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"No se encontró el archivo JSON: '{self.filepath}'")

        with open(self.filepath, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def modificar_y_guardar(self, nuevo_filepath: str):
        """Agrega el campo de estado a cada registro y guarda un nuevo JSON con json.dump."""
        data = self.leer_datos()

        # Modificación: agregar el campo de estado a cada registro
        # El dataset de Pokémon se exporta como una lista de objetos 
        if isinstance(data, list):
            for registro in data:
                if isinstance(registro, dict):
                    registro[self.CAMPO_ESTADO] = self.VALOR_ESTADO
        elif isinstance(data, dict):
            data[self.CAMPO_ESTADO] = self.VALOR_ESTADO

        # Guardar en un nuevo archivo con formato legible (indent=4);
        with open(nuevo_filepath, mode='w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Archivo JSON modificado guardado exitosamente en: '{nuevo_filepath}'")
        return nuevo_filepath