import pandas as pd
from datasets import load_dataset
from typing import Optional

class HFDatasetLoader:
    def __init__(self, dataset_name: str, split: Optional[str] = "train"):
        self.dataset_name = dataset_name
        self.split = split

    def load_as_dataframe(self) -> pd.DataFrame:
        try:
            dataset = load_dataset(self.dataset_name, split=self.split)
            return dataset.to_pandas()
        except Exception as e:
            raise RuntimeError(f"Error al cargar el dataset '{self.dataset_name}': {e}")
