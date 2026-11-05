import os
from datetime import datetime

class GeneradorResumenTxt:
    """Clase para generar un archivo .txt consolidado con los resultados reales
    de la ejecución de las clases de CSV y JSON."""

    def __init__(self, url_csv: str, url_json: str):
        self.url_csv = url_csv
        self.url_json = url_json
        self.detalles_ejecucion = []

    def registrar_proceso(self, formato: str, archivo_orig: str, archivo_nuevo: str,
                          modificacion: str, registros: int, clase: str, metodos: list):
        """Registra los metadatos y resultados de la ejecución de cada manejador.

        Los nombres de los parámetros coinciden con los keywords que usa main.py
        (archivo_orig, modificacion, registros).
        """
        info = {
            "formato": formato.upper(),
            "url_origen": self.url_csv if formato.lower() == "csv" else self.url_json,
            "archivo_original": archivo_orig,
            "archivo_nuevo": archivo_nuevo,
            "modificacion": modificacion,
            "registros": registros,
            "clase": clase,
            "metodos": metodos,
        }
        self.detalles_ejecucion.append(info)

    @staticmethod
    def _tamano_legible(ruta: str) -> str:
        """Devuelve el tamaño del archivo en KB/MB, o 'no disponible' si no existe."""
        if not os.path.exists(ruta):
            return "no disponible"
        tamano = os.path.getsize(ruta)
        if tamano >= 1024 * 1024:
            return f"{tamano / (1024 * 1024):.2f} MB"
        return f"{tamano / 1024:.2f} KB"

    def guardar_resumen(self, nombre_salida: str = "resumen_ejecucion.txt") -> str:
        """Genera el contenido estructurado y guarda el archivo de resumen .txt con datos reales."""
        contenido = []
        contenido.append("=" * 60)
        contenido.append("          INFORME DE EJECUCIÓN - TAREA DE DATOS          ")
        contenido.append("=" * 60)
        contenido.append("Dataset: Pokémon Classification Gen 1-9 (metadatos, sin imágenes)")
        contenido.append(f"Fecha y Hora de Ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for item in self.detalles_ejecucion:
            contenido.append(f"[{item['formato']}] PROCESAMIENTO DE ARCHIVO")
            contenido.append("-" * 40)
            contenido.append(f"• URL Específica de Origen:   {item['url_origen']}")
            contenido.append(f"• Archivo Importado (Orig):   {item['archivo_original']} "
                             f"({self._tamano_legible(item['archivo_original'])})")
            contenido.append(f"• Nuevo Archivo Guardado:     {item['archivo_nuevo']} "
                             f"({self._tamano_legible(item['archivo_nuevo'])})")
            contenido.append(f"• Modificación Aplicada:      {item['modificacion']}")
            contenido.append(f"• Registros Procesados:       {item['registros']}")
            contenido.append(f"• Clase Utilizada:            {item['clase']}")
            contenido.append(f"• Métodos Invocados:          {', '.join(item['metodos'])}")
            contenido.append("")

        contenido.append("=" * 60)
        contenido.append("               FIN DEL INFORME CONSOLIDADO               ")
        contenido.append("=" * 60)

        # Escritura usando rutas relativas y with open(...)
        with open(nombre_salida, "w", encoding="utf-8") as f:
            f.write("\n".join(contenido))

        print(f"Resumen consolidado generado exitosamente en: '{nombre_salida}'")
        return nombre_salida