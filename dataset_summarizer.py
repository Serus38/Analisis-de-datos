import pandas as pd
import io

class DatasetSummarizer:
    def __init__(self, dataframe: pd.DataFrame):
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("El objeto proporcionado debe ser un DataFrame.")
        self.df = dataframe

    def generate_summary(self) -> str:
        buffer = io.StringIO()

        buffer.write("==================================================\n")
        buffer.write("              RESUMEN DEL DATAFRAME               \n")
        buffer.write("==================================================\n\n")

        rows, cols = self.df.shape
        buffer.write("--- 1. DIMENSIONES ---\n")
        buffer.write(f"Cantidad de Filas:    {rows}\n")
        buffer.write(f"Cantidad de Columnas: {cols}\n\n")

        buffer.write("--- 2. ESTRUCTURA DE COLUMNAS Y VALORES NULOS ---\n")
        buffer.write(f"{'Nombre de Columna':<35} | {'Tipo de Dato':<12} | {'Valores Nulos':<13} | {'% Nulos':<8}\n")
        buffer.write("-" * 77 + "\n")

        for col in self.df.columns:
            dtype = str(self.df[col].dtype)
            null_count = self.df[col].isnull().sum()
            null_pct = (null_count / rows) * 100 if rows > 0 else 0
            buffer.write(f"{col:<35} | {dtype:<12} | {null_count:<13} | {null_pct:<7.2f}%\n")
        buffer.write("\n")

        buffer.write("--- 3. ESTADÍSTICAS DESCRIPTIVAS ---\n")
        num_df = self.df.select_dtypes(include=['number'])
        if not num_df.empty:
            buffer.write("\n[Variables Numéricas]\n")
            buffer.write(num_df.describe().T.to_string())
            buffer.write("\n\n")

        cat_df = self.df.select_dtypes(exclude=['number'])
        if not cat_df.empty:
            buffer.write("[Variables Categóricas / Texto]\n")
            buffer.write(cat_df.describe().T.to_string())
            buffer.write("\n\n")

        buffer.write("==================================================\n")
        buffer.write("               FIN DEL INFORME                    \n")
        buffer.write("==================================================\n")

        return buffer.getvalue()

    def save_summary_to_file(self, filename: str = "resumen_dataset.txt") -> str:
        summary_text = self.generate_summary()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(summary_text)
        print(f"Resumen guardado exitosamente en '{filename}'")
        return filename
