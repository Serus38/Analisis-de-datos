# EA2: Manejo de datos en CSV y JSON

## Descripción

En esta actividad se trabajó con un dataset de Pokémon de las generaciones 1 a 9. El objetivo fue practicar cómo:

- Descargar y preparar datos desde Hugging Face.
- Unir diferentes particiones de un dataset.
- Eliminar columnas que no son necesarias, como las imágenes.
- Leer y guardar información en formatos **CSV** y **JSON**.
- Modificar los datos sin alterar los archivos originales.
- Generar un resumen de la ejecución en un archivo de texto.

Dataset utilizado: [Pokemon Classification Gen 1-9](https://huggingface.co/datasets/JJMack/pokemon-classification-gen1-9).

## Archivos de la actividad

| Archivo | Función |
|---|---|
| `ManejoDatos.ipynb` | Coordina y muestra todo el proceso. |
| `manejador_csv.py` | Lee, modifica y guarda archivos CSV. |
| `manejador_json.py` | Lee, modifica y guarda archivos JSON. |
| `generador_resumen_txt.py` | Crea un informe de la ejecución. |

## ¿Qué se realizó?

### 1. Preparación del dataset

El notebook comprueba si los archivos locales ya existen. Si no existen, descarga el dataset desde Hugging Face y une las particiones `train`, `validation` y `test` en una sola tabla.

Después:

1. Se identifican y eliminan las columnas de tipo imagen.
2. Se conservan únicamente los metadatos de los Pokémon.
3. La información se exporta como `dataset_pokemon.csv` y `dataset_pokemon.json`.

### 2. Procesamiento del archivo CSV

La clase `ManejadorCSV` utiliza los módulos `csv` y `os` para:

1. Verificar que el archivo exista.
2. Leer los encabezados y las filas.
3. Agregar el registro de **MissingNo** si todavía no está incluido.
4. Guardar el resultado en `dataset_pokemon_modificado.csv`.

El archivo original se conserva sin cambios.

### 3. Procesamiento del archivo JSON

La clase `ManejadorJSON` utiliza los módulos `json` y `os` para:

1. Leer el contenido del archivo JSON.
2. Agregar el campo:

```json
"estado_revision": "verificado_gen1_9"
```

El campo se agrega a cada registro cuando el JSON contiene una lista de objetos. El resultado se guarda en `dataset_pokemon_modificado.json`.

### 4. Generación del resumen

Finalmente, `GeneradorResumenTxt` reúne información sobre cada proceso, como:

- Formato trabajado.
- Archivo de origen y archivo nuevo.
- Modificación aplicada.
- Cantidad de registros.
- Clase y métodos utilizados.
- Tamaño de los archivos.

El informe se guarda como `resumen_ejecucion.txt`.

## Flujo general

```text
Dataset de Hugging Face
          |
          v
Archivos originales CSV y JSON
          |
          +--> ManejadorCSV  --> dataset_pokemon_modificado.csv
          |
          +--> ManejadorJSON --> dataset_pokemon_modificado.json
          |
          v
     resumen_ejecucion.txt
```

## ¿Cómo ejecutar la actividad?

1. Abrir la carpeta `EA2` en Visual Studio Code o Jupyter Notebook.
2. Abrir `ManejoDatos.ipynb`.
3. Instalar las dependencias necesarias si el entorno aún no las tiene:

```bash
pip install datasets pandas
```

4. Ejecutar las celdas del notebook en orden.
5. Revisar los archivos generados al finalizar.

La primera ejecución puede tardar más porque descarga el dataset. En ejecuciones posteriores se reutilizan los archivos locales si ya existen.

## Resultado esperado

Al terminar correctamente, se muestran mensajes similares a los siguientes:

```text
Archivo CSV modificado guardado exitosamente en: 'dataset_pokemon_modificado.csv'
Archivo JSON modificado guardado exitosamente en: 'dataset_pokemon_modificado.json'
Resumen consolidado generado exitosamente en: 'resumen_ejecucion.txt'
```

## Aprendizajes

Con esta actividad se practicó:

- La organización del código mediante clases.
- La lectura y escritura de archivos estructurados.
- El uso de `csv.reader`, `csv.writer`, `json.load` y `json.dump`.
- La validación de rutas y archivos.
- La creación de archivos nuevos para conservar los datos originales.
- La documentación de un proceso de transformación de datos.

